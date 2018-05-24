from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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


class Repository:

    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://root:srv18180@localhost/serverdb')
        self.session = self.get_session()
        self.create_base()

    def create_base(self):
        CBase.metadata.create_all(self.engine)

    def get_session(self):
        Session = sessionmaker(bind= self.engine)
        session = Session()
        return session

    def add(self, obj):
        try:
            self.session.add(obj)
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return None


    def get_user(self, username):
        result = self.session.query(Users).filter_by(username = username).first()
        return result

if __name__ == '__main__':
    rep = Repository()
    # rep.add(Users('pilik', '1234','pilik@mail.ru'))
    print(rep.get_user('pilik').password)
