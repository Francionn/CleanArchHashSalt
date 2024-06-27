from src.domain.use_cases.user_delete import UserDelete as UserDeleteInterface
from src.data.interfaces.user_repository import UserRepositoryInterface
from src.erros.types.http_not_found import HttpNotFoundError


class UserDelete(UserDeleteInterface):
    
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def delete(self, id: int) -> None:
        self.__check_delete(id)

    def __check_delete(self, id: int):
        try:
            self.__user_repository.delete(id)
        except Exception as exception:
            raise HttpNotFoundError('Not found user')
    