import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


class OpenAIProvider:

    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        self.api_key = os.getenv("OPENAI_API_KEY")

        self.llm = ChatOpenAI(
            model=self.model,
            api_key=self.api_key
        )

    def get_llm(self):
        return self.llm