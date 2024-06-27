from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.orm import relationship

from src.infra.db.settings.base import Base
from src.infra.db.entities.users_password import Userpassword


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, unique=True)

    userpasswords = relationship('Userpassword', back_populates='user', cascade='all, delete')

    __table_args__ = (Index('idx_user_email'),)

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.userpasswords = []
        self.userpasswords.append(Userpassword(password))  
    
    def __repr__(self):
        return f'Nome: {self.name} / Password: {self.userpasswords} / Email: {self.email}'
