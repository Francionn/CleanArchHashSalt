from src.domain.use_cases.user_login import UserLogin as UserLoginInterface
from src.data.interfaces.user_repository import UserRepositoryInterface
from src.erros.types.http_not_found import HttpNotFoundError


class UserLogin(UserLoginInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
    
    def login_validator(self, email:str, password:str) -> bool:
    
        return self.__check_login(email,password)
    
    def __check_login(self, email, password) -> bool:
        validator = self.__user_repository.login(email,password)
        
        if not validator:
            raise HttpNotFoundError('Invalid email or password')
        return validator
