from openai import OpenAI

from config import settings

class ContentClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate(self,prompt,system = None ):
        message = []
        if system:
            message.append({"role": "system", "content": system})
        message.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(model=settings.OPENAI_MODEL, 
                                                       messages=message)        
        return response.choices[0].message.content
    