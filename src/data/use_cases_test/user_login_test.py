from ..use_cases.user_login import UserLogin

from src.infra.db.test.user_repository import UserRepositorySpy


def test_login():
    name = 'anyname'
    password = 'anypw'

    repository = UserRepositorySpy()
    user_login = UserLogin(repository)

    response = user_login.login_validator(name, password)
