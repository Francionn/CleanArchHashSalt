import bcrypt

from sqlalchemy.orm.exc import NoResultFound

from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import User


class UserRepository:
    def create_user(self, name, password, email):   
        with DBConnectionHandler() as db:
            try:    
                data = User(name, password, email)
                db.session.add(data)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception    
    
    def login(self, email, password):
        with DBConnectionHandler() as db:
            try:    
                user = db.session.query(User).filter_by(email = email).first()
                hashed = str(user.userpasswords[0])
                return UserRepository.check_password(password, hashed) 
            except Exception as exception:
                db.session.rollback()
                raise exception 
    
    def delete(self, id):
        with DBConnectionHandler() as db:
            try:    
                db.session.query(User).filter(User.id == id).delete()
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def get_name(self, email):
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
    
    
    @staticmethod    
    def check_password(password, hashed):    
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    