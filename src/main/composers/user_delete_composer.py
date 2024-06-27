from src.infra.db.repositories.users_repository import UserRepository
from src.data.use_cases.user_delete import UserDelete
from src.presentation.controllers.user_delete_controller import UserDeleteController

def user_delete_composer():
    repository = UserRepository()
    use_case = UserDelete(repository)
    controller = UserDeleteController(use_case)
    
    return controller.handle