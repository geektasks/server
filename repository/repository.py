from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from repository.users import Users

CBase = declarative_base()

class Repository:

    def __init__(self):
        self.engine = create_engine('mysql+mysqlconnector://serv_root:srv18180@10.72.72.30/serverdb')
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

    def get_pass(self,username):
        result = self.session.query(Users).filter_by(username = username).first().password
        return result

    def set_session_id(self,username,session_id):
        try:
            self.session.query(Users).filter_by(username=username).first().session_id = session_id
            self.session.commit
            return 1
        except Exception as err:
            self.session.rollback()
            return err

if __name__ == '__main__':
    rep = Repository()
    # rep.add(Users('pilik', '1234','pilik@mail.ru'))
    print(rep.get_user('pilik').password)
    print(rep)