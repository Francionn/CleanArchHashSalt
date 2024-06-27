from abc import ABC, abstractmethod

class UserDelete(ABC):
    
    @abstractmethod
    def delete(self, id:str) -> None: pass
    