from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.user_login import UserLogin as UserLoginInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserLoginController(ControllerInterface):
    
    def __init__(self, use_case: UserLoginInterface) -> None:
        self.__user_case = use_case

    def handle(self, http_request: HttpRequest ) -> HttpResponse:
        email = http_request.body.get("email")
        password = http_request.body.get("password")
        
        if not email or not password:
            return HttpResponse(status_code=400, body={"error": "Missing email or password"})

        response = self.__user_case.login_validator(email, password)
        
        return HttpResponse(
            status_code=200,
            body = {"data": response}
            )
    