from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

CBase = declarative_base()

class Users(CBase):

    __tablename__ = 'users'
    username = Column(VARCHAR(45), primary_key= True, nullable= False, unique= True)
    password = Column(LONGTEXT, nullable= False)
    email = Column(VARCHAR(45), nullable= True)

    def __init__(self, username, password, email = None):
        self.username = username
        self.password = password
        self.email = email
    def __repr__(self):
        return self.username