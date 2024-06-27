from src.presentation.interfaces.controller_interface import ControllerInterface
from src.data.use_cases.user_name import UserName as UserNameInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class UserNameController(ControllerInterface):
    
    def __init__(self, use_case: UserNameInterface) -> None:
        self.__user_case = use_case

    def handle(self, http_request: HttpRequest ) -> HttpResponse:
        email = http_request.body.get("email")

        response = self.__user_case.name_finder(email)
        return HttpResponse(
            status_code=200,
            body = {"data": response}
            )
