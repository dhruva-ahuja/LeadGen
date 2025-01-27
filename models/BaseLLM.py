class BaseLLM:
    def completions(self, prompt: str) -> dict:
        raise NotImplementedError("This method should be implemented by the subclass")
