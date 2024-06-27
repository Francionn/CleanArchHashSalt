from abc import ABC, abstractmethod

class UserName(ABC):
    
    @abstractmethod
    def name_finder(self, email:str) -> str: pass
    