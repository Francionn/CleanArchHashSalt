from src.infra.db.test.user_repository import UserRepositorySpy
from src.data.use_cases.user_name import UserName

def test_name():
    email = 'any@teste.com'
    
    repository = UserRepositorySpy()
    user_name= UserName(repository)

    user_name.name_finder(email)
