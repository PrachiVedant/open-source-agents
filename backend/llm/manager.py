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
        self.config = config or {}

    def get_llm(self):
        llm_config = self.config.get("llm") or {}
        provider = str(llm_config.get("provider", "")).lower()
        model = llm_config.get("model")

        if not provider:
            raise ValueError("LLM provider is missing from the agent config.")

        provider_class = self.PROVIDERS.get(provider)

        if provider_class is None:
            supported = ", ".join(self.PROVIDERS.keys())
            raise ValueError(
                f"Unsupported LLM provider: '{provider}'. "
                f"Supported providers: {supported}"
            )

        if not model:
            raise ValueError("LLM model is missing from the agent config.")

        return provider_class(model).get_llm()