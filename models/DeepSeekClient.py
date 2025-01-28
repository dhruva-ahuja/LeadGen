from openai import OpenAI

from models.BaseLLM import BaseLLM

class DeepSeekClient(BaseLLM):
    def __init__(self, api_key):
        self.api_key = api_key
        self.model = OpenAI(api_key=self.api_key,
                            base_url="https://api.deepseek.com")
    
    def completions(self, prompt: str) -> dict:
        response = self.model.chat.completions.create(
            model="deepseek-chat",  # Specify the model
            messages=[
                {"role": "system", "content": """You are a highly knowledgeable financial assistant. 
                 You provide accurate and detailed financial data and KPIs for the given companies. 
                 Use the appropriate tools to fetch real-time data when needed. Send output as JSON 
                 with KPI as key and its value."""},  # Set the context
                {"role": "user", "content": prompt}   # User's prompt
            ],
            max_tokens=100  # Limit the response length
        )
        return response