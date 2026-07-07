import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


class GroqProvider:

    def __init__(self, model: str = "llama-3.3-70b-versatile"):
        self.model = model
        self.api_key = os.getenv("GROQ_API_KEY")

        self.llm = ChatGroq(
            model=self.model,
            api_key=self.api_key
        )

    def get_llm(self):
        return self.llm