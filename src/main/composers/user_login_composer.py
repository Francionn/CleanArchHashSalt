from src.infra.db.repositories.users_repository import UserRepository
from src.data.use_cases.user_login import UserLogin
from src.presentation.controllers.user_login_controller import UserLoginController


def user_login_composer():
    repository = UserRepository()
    use_case = UserLogin(repository)
    controller = UserLoginController(use_case)

    return controller.handle