from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from repository.models_users import Users
from repository.models_tasks import Tasks

from repository.db_core import CBase


class Performers(CBase):
    __tablename__ = 'performers'
    id = Column(INTEGER(), primary_key=True, autoincrement=True)
    user_id = Column(INTEGER(), ForeignKey('users.user_id'), nullable=False)
    task_id = Column(INTEGER(), ForeignKey('tasks.task_id'), nullable=False)

    user = relationship(Users, foreign_keys=[user_id])
    task = relationship(Tasks, foreign_keys=[task_id])

    def __repr__(self):
        return '{} {}'.format(self.user_id, self.task_id)


if __name__ == '__main__':
    pass
