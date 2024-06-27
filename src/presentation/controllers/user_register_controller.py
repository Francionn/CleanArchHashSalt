from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.user_register import UserRegister as UserRegisterInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserRegisterController(ControllerInterface):
    
    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__user_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        if http_request.body is None:
            return HttpResponse(status_code=400, body={"error": "Missing request body"})

        name = http_request.body.get("name")
        password = http_request.body.get("password")
        email = http_request.body.get("email")

        if name is None or password is None or email is None:
            return HttpResponse(status_code=400, body={"error": "Invalid request body"})

        response = self.__user_case.register(name, password, email)
        return HttpResponse(
            status_code=200,
            body={"data": response}
        )
