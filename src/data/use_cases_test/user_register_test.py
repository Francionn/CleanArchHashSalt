from ..use_cases.user_register import UserRegister

from src.infra.db.test.user_repository import UserRepositorySpy

def test_register():
    name = 'anyname'
    password = '@@11a1a11aanypw'
    email = 'any@email.com'

    repository = UserRepositorySpy()
    user_register = UserRegister(repository)
    
    response = user_register.register(name, password,  email)
