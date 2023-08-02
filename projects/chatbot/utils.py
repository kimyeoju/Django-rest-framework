import openai
from django.conf import settings


openai.api_key = settings.APIKEY


def gpt_chat(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0.5,
        n=5,
        max_tokens=1024,
        stop=None,
    )
    return response["choices"][0]["message"]["content"]