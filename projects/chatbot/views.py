from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from dotenv import load_dotenv
import openai
import os
from .models import Conversation

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatbotView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    def post(self, request, *args, **kwargs):
        # 사용자 user당 횟수 제한

        prompt = request.data.get('prompt')
        if prompt:
            # 이전 대화 기록 가져오기
            session_conversations = request.session.get('conversations', [])
            previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            conversation = Conversation(prompt=prompt, response=response, user=request.user)
            conversation.save()
            
            return Response({'response': response}, status=status.HTTP_200_OK)

        return Response({'error': 'No prompt provided.'}, status=status.HTTP_400_BAD_REQUEST)
        