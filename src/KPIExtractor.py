import pandas as pd

from models.BaseLLM import BaseLLM
from src.utils import get_kpi_list

class KPIExtractor:
    def __init__(self, llm_client: BaseLLM):
        self.llm_client = llm_client

    def extract_kpis(self, customer_list: list):
        kpi_values = []
        for customer in customer_list:
            prompt = self.build_prompt(customer)
            response = self.llm_client.completions(prompt)
            kpi_values.append(self.parse_kpi_response(response))
        return pd.DataFrame(kpi_values)

    def build_prompt(self, customer: str):
        prompt = f"""Extract the following KPIs for the {customer} below:\nKPIs:\n        
        - {'\n- '.join(get_kpi_list())}"""
        print(prompt)
        return prompt
    
    def parse_kpi_response(self, response):
        try:
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error parsing response: {e}")
            return {}