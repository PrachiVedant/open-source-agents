from backend.memory.registry import MEMORY_REGISTRY

class MemoryManager:
    def __init__(self,config):
        self.config=config

    def get_memory(self):
        memory_type=self.config["memory"]["type"]
        memory_class=MEMORY_REGISTRY.get(memory_type)
        if memory_class is None:
            raise ValueError(f"Memory type '{memory_type}' is not registered.")
        return memory_class()
    