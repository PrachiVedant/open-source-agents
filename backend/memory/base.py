from abc import ABC, abstractmethod

class BaseMemory(ABC):
    @abstractmethod
    def load(self,session_id:str):
        pass

    @abstractmethod
    def save(self,session_id:str,data:dict):
        pass

    @abstractmethod
    def clear(self,session_id:str):
        pass
