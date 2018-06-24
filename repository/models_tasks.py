from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from repository.models_users import Users

from repository.db_core import CBase


# TODO добавить поля time / deadline
class Tasks(CBase):
    __tablename__ = 'tasks'
    task_id = Column(INTEGER(), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(45), nullable=False, unique=False)
    description = Column(LONGTEXT, nullable=True)
    status = Column(INTEGER(), nullable=False)
    creator_id = Column(INTEGER(), ForeignKey('users.user_id'), nullable=False)
    date_create = Column(VARCHAR(25))
    date_deadline = Column(VARCHAR(25))
    date_reminder = Column(VARCHAR(25))
    time_reminder = Column(VARCHAR(25))

    creator = relationship(Users, foreign_keys=[creator_id])

    def __init__(self, creator_id, name, status=0, description=None, date_create=None, date_deadline=None,
                 date_reminder=None, time_reminder=None):
        self.creator_id = creator_id
        self.name = name
        self.status = status
        self.description = description
        self.date_create = date_create
        self.date_deadline = date_deadline
        self.date_reminder = date_reminder
        self.time_reminder = time_reminder

    def __repr__(self):
        return '{} {}'.format(self.name, self.description)


if __name__ == '__main__':
    pass
