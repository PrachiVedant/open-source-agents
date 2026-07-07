import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama


load_dotenv()


class OllamaProvider:

    def __init__(self, model: str = "llama3.1", base_url: str | None = None):
        self.model = model

        # Priority: explicit arg > OLLAMA_HOST env > OLLAMA_BASE_URL env > default
        host = base_url or os.getenv("OLLAMA_HOST") or os.getenv("OLLAMA_BASE_URL") or "http://127.0.0.1:11435"

        # Ensure scheme is present
        if host and not host.startswith("http"):
            host = "http://" + host

        self.llm = ChatOllama(
            model=self.model,
            temperature=0,
            base_url=host,
        )

    def get_llm(self):
        return self.llm