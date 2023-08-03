from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Conversation
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .utils import gpt_chat
import json

# Create your views here.


class ChatbotView(APIView):
    permission_classes = [IsAuthenticated] # 인증된 user만 접근 가능
    throttle_classes = [UserRateThrottle] # 호출 제한

    def post(self, request):
        request_data_utf8 = request.body.decode('utf-8')
        request_data = json.loads(request_data_utf8)
        if request_data:
            response = gpt_chat(request_data)
            conversation = Conversation(
                prompt=request_data, response=response, user=request.user)
            conversation.save()
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
