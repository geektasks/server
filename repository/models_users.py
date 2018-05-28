from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

CBase = declarative_base()

class Users(CBase):

    __tablename__ = 'users'
    user_id = Column(INTEGER(), primary_key = True,autoincrement=True)
    username = Column(VARCHAR(45), nullable= False, unique= True)
    password = Column(LONGTEXT, nullable= False)
    email = Column(VARCHAR(45), nullable= True)
    session_id = Column(INTEGER())

    def __init__(self, user_id,username, password, email = None, session_id=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.session_id= session_id
    def __repr__(self):
        return self.username