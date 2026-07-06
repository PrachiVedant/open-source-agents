from backend.llm.openai import OpenAIProvider


class LLMManager:
    def __init__(self,config):
        self.config=config

    def get_llm(self):
        provider=self.config["llm"]["provider"]
        model=self.config["llm"]["model"]

        if provider=="openai":
            return OpenAIProvider(model).get_llm()
        
        raise ValueError(f"Unsupported LLM provider: {provider}")