from src.infra.db.repositories.users_repository import UserRepository
from src.data.use_cases.user_name import UserName
from src.presentation.controllers.user_name_controller import UserNameController

def user_name_composer():
    repository = UserRepository
    use_case = UserName(repository)
    controller = UserNameController(use_case)

    return controller.handle