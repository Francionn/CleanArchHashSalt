from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.user_repository import UserRepositoryInterface
from src.data.validators.email_validator import EmailValidators
from src.data.validators.password_validator import PasswordValidator
from src.erros.types.http_bad_request import HttpBadRequestError


class UserRegister(UserRegisterInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def register(self, name: str, password: str, email: str):
        self.__email_validator(email)
        self.__password_validator(password)
        self.__create_user(name, password, email)
        return True
    
    @classmethod
    def __email_validator(cls, email:str) -> bool:
        check_email = EmailValidators.validate(email)
        
        if not check_email:
            raise HttpBadRequestError('Invalid email')
        return check_email
    
    @classmethod
    def __password_validator(cls, password:str) -> bool:
        check_pw = PasswordValidator.validate(password)

        if not check_pw:
            raise HttpBadRequestError('Invalid password')
        return check_pw 
    
    def __create_user(self,name: str, password: str, email: str) -> None:
        self.__user_repository.create_user(name, password, email)
