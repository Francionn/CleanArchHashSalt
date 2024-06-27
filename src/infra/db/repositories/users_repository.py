import bcrypt

from sqlalchemy.orm.exc import NoResultFound

from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import User
from src.data.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    
    @classmethod
    def create_user(cls, name: str, password: str, email: str) -> bool:   
        with DBConnectionHandler() as db:
            try:    
                data = User(name, password, email)
                db.session.add(data)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception    
    
    @classmethod
    def login(cls, email: str, password: str) -> bool:
        with DBConnectionHandler() as db:
            try:    
                user = db.session.query(User).filter_by(email = email).first()
                hashed = str(user.userpasswords[0])
                return UserRepository.__check_password(password, hashed) 
            except Exception as exception:
                db.session.rollback()
                raise exception 
    
    @classmethod
    def delete(cls, id: int) -> None:
        with DBConnectionHandler() as db:
            try:    
                db.session.query(User).filter(User.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    @classmethod
    def get_name(cls, email: str) -> str:
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(User).filter_by(email = email).first()
                user = str(data.name)
                return user
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    @classmethod  
    def __check_password(cls, password, hashed):    
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    