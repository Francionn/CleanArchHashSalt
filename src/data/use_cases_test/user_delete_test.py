from src.infra.db.test.user_repository import UserRepositorySpy
from ..use_cases.user_delete import UserDelete

def test_delete():
    id = 1
    
    repository = UserRepositorySpy()
    user_delete = UserDelete(repository)

    user_delete.delete(id)
