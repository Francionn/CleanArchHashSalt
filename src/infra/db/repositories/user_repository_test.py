import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from .users_repository import UserRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason='Sensitive test')
def test_insert_user():
    mocked_name = 'first'
    mocked_password = '@1github11@'
    mocked_email = 'name@exammple.com'

    users_repository = UserRepository()
    users_repository.create_user(mocked_name, mocked_password, mocked_email)

    sql = '''
        SELECT u.id, u.name, u.email, p.passwordhash
        FROM users u
        JOIN userpasswords p ON u.id = p.user_id
        WHERE u.name = '{}'
        AND u.email = '{}'
        AND p.passwordhash = '{}'
    '''.format(mocked_name, mocked_email, mocked_password)
    
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.lemail == mocked_email
    assert registry.password == mocked_password
    
    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))
    connection.commit()
