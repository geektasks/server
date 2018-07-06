from sqlalchemy import Column
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from repository.models_users import Users
from repository.models_tasks import Tasks
from repository.models_comments import Comments
from repository.models_performers import Performers
from repository.models_watchers import Watchers

from repository.db_core import CBase
from serv.create_config import get_setting


class Repository:

    def __init__(self):
        path = 'settings.ini'
        username = get_setting(path, 'Database', 'username')
        password = get_setting(path, 'Database', 'password')
        host = get_setting(path, 'Database', 'host')
        db = get_setting(path, 'Database', 'db')

        self.engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.format(username, password, host, db))
        self.session = self.get_session()
        self.create_base()

    def create_base(self):
        CBase.metadata.create_all(self.engine)

    def get_session(self):
        Session = sessionmaker(bind=self.engine)
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

    def del_(self, obj):
        try:
            self.session.delete(obj)
            self.session.commit()
            return True
        except Exception as err:
            print('delete exception', err)
            self.session.rollback()
            return None

    def get_user(self, username):
        result = self.session.query(Users).filter_by(username=username).first()
        return result

    def get_user_by_user_id(self, user_id):
        result = self.session.query(Users).filter_by(user_id=user_id).first()
        return result

    def get_user_by_session_id(self, session_id):
        self.session.commit()
        result = self.session.query(Users).filter_by(session_id=session_id).first()
        return result

    def get_pass(self, username):
        result = self.session.query(Users).filter_by(username=username).first().password
        print('get pass result', result)
        return result

    def set_session_id(self, username, session_id):
        try:
            # TODO сделать проверку на уникальность session_id
            self.session.query(Users).filter_by(username=username).first().session_id = session_id
            print(self.session.query(Users).filter_by(username=username).first().session_id)
            self.session.commit()
            return 1
        except Exception as err:
            self.session.rollback()
            return err

    def get_task(self, name):
        result = self.session.query(Tasks).filter_by(name=name).first()
        return result

    def get_all_tasks(self, creator_id):
        result = self.session.query(Tasks).filter_by(creator_id=creator_id).all()
        return result

    def get_task_by_task_id(self, task_id):
        return self.session.query(Tasks).filter_by(task_id=task_id).first()

    def edit_task(self, task_id, attr, value):
        '''

        :param task_id:
        :param attr: 'description' or 'name' or 'status' or 'date_reminder' or 'time_reminder' or 'date_deadline'
        :param value: new value
        :return:
        '''
        try:
            task = self.get_task_by_task_id(task_id)
            if attr == 'description':
                task.description = value
            if attr == 'name':
                task.name = value
            if attr == 'status':
                task.status = value
            if attr == 'date_reminder':
                task.date_reminder = value
            if attr == 'time_reminder':
                task.time_reminder = value
            if attr == 'date_deadline':
                task.date_deadline = value
            self.session.commit()
            return True
        except:
            self.session.rollback()
            return False

    def get_comment(self, user_id, task_id, time):
        return self.session.query(Comments).filter_by(user_id=user_id, task_id=task_id, time=time).first()

    def get_comment_by_comment_id(self, comment_id):
        return self.session.query(Comments).filter_by(comment_id=comment_id).first()

    def get_comments(self, task_id):
        '''
        ??обновлять омментарии на клиенте либо запросом на один комментарий, либо запросом сразу на все комментарии задачи??
        :param task_id: server_task_id
        :return:?? {task_id: {comment_id_1: {...}, comment_id_2: {...}, ...}} or [{'id': comment.comment_id,'user': user, 'text': comment.text, 'time': comment.time}, ...]
        '''
        # comments_list = list()
        # comments = self.session.query(Comments).filter_by(task_id=task_id).all()
        # for comment in comments:
        #     if comment.task_id == task_id:
        #         user = self.session.query(Users).filter_by(user_id=comment.user_id).first().username
        #         comments_list.append(
        #             {'id': comment.comment_id, 'user': user, 'text': comment.text, 'time': comment.time})
        # return comments_list
        comments_dict = {task_id: {}}
        comments = self.session.query(Comments).filter_by(task_id=task_id).all()
        for comment in comments:
            comment_id = comment.comment_id
            text = comment.text
            time = comment.time
            user = self.session.query(Users).filter_by(user_id=comment.user_id).first().username
            comments_dict[task_id].update({comment_id: {'user': user, 'text': text, 'time': time}})
        return comments_dict

    def get_watcher(self, task_id, user_id):
        return self.session.query(Watchers).filter_by(task_id=task_id, user_id=user_id).first()

    def get_performer(self, task_id, user_id):
        return self.session.query(Performers).filter_by(task_id=task_id, user_id=user_id).first()

    def get_all_users(self):
        return self.session.query(Users).all()

    def get_all_performers(self, task_id):
        return self.session.query(Performers).filter_by(task_id=task_id).all()

    def get_all_watchers(self, task_id):
        return self.session.query(Watchers).filter_by(task_id=task_id).all()


if __name__ == '__main__':
    rep = Repository()
    # rep.add(Users('pilik', '1234','pilik@mail.ru'))
    # print(rep.get_user('pilik').session_id)
    # print(rep)
