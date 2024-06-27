from src.domain.use_cases.user_name import UserName as UserNameInterface
from src.data.interfaces.user_repository import UserRepositoryInterface
from src.erros.types.http_not_found import HttpNotFoundError
from src.erros.erro_handle import handle_errors

class UserName(UserNameInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
    
    def name_finder(self, email:str) -> str:
        return self.__get_name(email)
    
    def __get_name(self, email:str) -> str:
        try:
            return self.__user_repository.get_name(email)
        except Exception as exception:
            raise handle_errors(exception)
       