from backend.llm.openai import OpenAIProvider
from backend.llm.groq import GroqProvider
from backend.llm.ollama import OllamaProvider


class LLMManager:

    PROVIDERS = {
        "openai": OpenAIProvider,
        "groq": GroqProvider,
        "ollama": OllamaProvider,
    }

    def __init__(self, config):
        self.config = config

    def get_llm(self):
        provider = self.config["llm"]["provider"].lower()
        model = self.config["llm"]["model"]

        provider_class = self.PROVIDERS.get(provider)

        if provider_class is None:
            supported = ", ".join(self.PROVIDERS.keys())
            raise ValueError(
                f"Unsupported LLM provider: '{provider}'. "
                f"Supported providers: {supported}"
            )

        return provider_class(model).get_llm()