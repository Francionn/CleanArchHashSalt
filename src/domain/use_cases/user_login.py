from abc import ABC, abstractmethod

class UserLogin(ABC):
    
    @abstractmethod
    def login_validator(self, email:str, password:str) -> bool: pass
    