from dotenv import load_dotenv
import os

"""Project configuration helper.

Loads environment variables and exposes a `config` dictionary used across
the backend. Defaults are conservative and match development setup.
"""

load_dotenv()

config = {
    "llm": {
        "provider": os.getenv("LLM_PROVIDER", "ollama"),
        "model": os.getenv("LLM_MODEL", "llama3.1"),
    },
    "memory": {
        # supported: "in_memory"
        "type": os.getenv("MEMORY_TYPE", "in_memory"),
    },
}

__all__ = ["config"]
