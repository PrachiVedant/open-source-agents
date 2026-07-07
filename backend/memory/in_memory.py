from backend.memory.base import BaseMemory

class InMemory(BaseMemory):
    def __init__(self):
        self.memory={}

    def load(self, session_id: str):
        return self.memory.get(session_id,[])
    def save(self, session_id: str, messages):
        self.memory[session_id] = messages
    def clear(self, session_id: str):
        if session_id in self.memory:
            del self.memory[session_id]

