from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def create_user(self, name: str, password: str, email: str) -> bool :pass   
            
    @abstractmethod
    def login(self, email: str, password: str) -> bool:pass  
        
    @abstractmethod
    def delete(self, id: int) -> None:pass  
        
    @abstractmethod
    def get_name(self, email: str) -> str:pass  
