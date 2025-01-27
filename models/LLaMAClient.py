from transformers import LlamaForCausalLM, LlamaTokenizer

from models.BaseLLM import BaseLLM

class LLaMAClient(BaseLLM):
    def __init__(self, model_path):
        # Example: Load the LLaMA model (assuming you're using a library like Hugging Face)
        self.tokenizer = LlamaTokenizer.from_pretrained(model_path)
        self.model = LlamaForCausalLM.from_pretrained(model_path)

    def completions(self, prompt: str) -> dict:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=100)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"response": response}
