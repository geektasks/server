from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from repository.models_users import Users
from repository.models_tasks import Tasks

from repository.db_core import CBase


class Comments(CBase):
    __tablename__ = 'comments'
    comment_id = Column(INTEGER(), primary_key=True, autoincrement=True)
    text = Column(LONGTEXT, nullable=False)
    time = Column(VARCHAR(25), nullable=False)
    user_id = Column(INTEGER(), ForeignKey('users.user_id'), nullable=False)
    task_id = Column(INTEGER(), ForeignKey('tasks.task_id'), nullable=False)

    user = relationship(Users, foreign_keys=[user_id])
    task = relationship(Tasks, foreign_keys=[task_id])

    def __init__(self, text, time, user_id, task_id):
        self.text = text
        self.time = time
        self.user_id = user_id
        self.task_id = task_id

    def __repr__(self):
        return '{} {}'.format(self.text, self.time)


if __name__ == '__main__':
    pass
