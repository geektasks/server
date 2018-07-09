from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER, TINYINT
from sqlalchemy.orm import relationship
from repository.models_users import Users
from repository.models_tasks import Tasks
from repository.models_watchers import Watchers
from repository.models_performers import Performers
from repository.models_comments import Comments

from repository.db_core import CBase


class Rights(CBase):
    __tablename__ = 'rights'
    right_id = Column(INTEGER(), primary_key=True, autoincrement=True)
    task_id = Column(INTEGER(), ForeignKey('tasks.task_id'), nullable=True)
    user_id = Column(INTEGER(), ForeignKey('users.user_id'), nullable=True)

    status = Column(TINYINT(), nullable=True)
    name = Column(TINYINT(), nullable=True)
    description = Column(TINYINT(), nullable=True)
    comments = Column(TINYINT(), nullable=True)
    date_deadline = Column(TINYINT(), nullable=True)
    date_reminder = Column(TINYINT(), nullable=True)
    time_reminder = Column(TINYINT(), nullable=True)

    task = relationship(Tasks, foreign_keys=[task_id])
    user = relationship(Users, foreign_keys=[user_id])

    def __init__(self, task_id, user_id, status=0, name=0, description=0, comments=0, date_deadline=0,
                 date_reminder=0, time_reminder=0):
        self.task_id = task_id
        self.user_id = user_id
        self.name = name
        self.status = status
        self.description = description
        self.comments = comments
        self.date_deadline = date_deadline
        self.date_reminder = date_reminder
        self.time_reminder = time_reminder

    def __repr__(self):
        return '{} {}'.format(self.task_id, self.user_id)


if __name__ == '__main__':
    pass
