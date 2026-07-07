import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so package imports work when running
# this file directly (e.g. `python testmemory.py`).
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
load_dotenv()

from config.config import config
from backend.memory.manager import MemoryManager

memory = MemoryManager(config).get_memory()

memory.save(
    "user1",
    ["Hello", "How are you?"]
)

print(memory.load("user1"))

memory.clear("user1")