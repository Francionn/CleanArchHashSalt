import bcrypt

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.infra.db.settings.base import Base
from src.validators.password_register_validator import PasswordValidator


class Userpassword(Base):
    __tablename__ = "userpasswords"

    userpassword_id = Column(Integer, primary_key=True, autoincrement=True)
    passwordhash = Column(String(255), nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = relationship('User', back_populates='userpasswords')

    def __init__(self, password):     
        self.passwordhash = None
        self.raw_password = password
    
    @property
    def raw_password(self):
        return self.passwordhash

    @raw_password.setter
    def raw_password(self, password):
        if PasswordValidator.validate(password):
            self.passwordhash = self.hash_password(password)
    
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def __repr__(self):
        return self.passwordhash
    