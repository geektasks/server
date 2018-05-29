from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

from repository.db_core import CBase

class Users(CBase):

    __tablename__ = 'users'
    user_id = Column(INTEGER(), primary_key = True,autoincrement=True)
    username = Column(VARCHAR(45), nullable= False, unique= True)
    password = Column(LONGTEXT, nullable= False)
    email = Column(VARCHAR(45), nullable= True)
    session_id = Column(INTEGER())

    def __init__(self, username, password, email = None, session_id=None):
        self.username = username
        self.password = password
        self.email = email
        self.session_id= session_id
    def __repr__(self):
        return self.username