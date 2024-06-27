from abc import ABC, abstractmethod

class UserRegister(ABC):
    
    @abstractmethod
    def register(self, name:str, password:str, email:str) -> bool: pass
    