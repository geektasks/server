from sqlalchemy import create_engine, Column, Integer, String, Unicode, BLOB, Boolean, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from repository.models import Users

CBase = declarative_base()

class Repository:

    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://serv_root:srv18180@localhost/serverdb')
        self.session = self.get_session()
        # self.create_base()

    def create_base(self):
        CBase.metadata.create_all(self.engine)

    def get_session(self):
        Session = sessionmaker(bind= self.engine)
        session = Session()
        return session

    def add(self, obj):
        self.session.add(obj)
        self.session.commit()


    def get_user(self, username):
        result = self.session.query(Users).filter_by(username = username).first()
        return result

if __name__ == '__main__':
    rep = Repository()
    # rep.add(Users('pilik', '1234','pilik@mail.ru'))
    print(rep.get_user('pilik').password)
