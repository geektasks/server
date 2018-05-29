from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT, VARCHAR, INTEGER
from sqlalchemy.orm import relationship
from repository.models_users import Users

from repository.db_core import CBase


class Tasks(CBase):
    __tablename__ = 'tasks'
    task_id = Column(INTEGER(), primary_key=True, autoincrement=True)
    name = Column(VARCHAR(45), nullable=False, unique=True)
    description = Column(LONGTEXT, nullable=True)
    status = Column(INTEGER(), nullable=False)
    creator_id = Column(INTEGER(), ForeignKey('users.user_id'), nullable=False)
    # watcher_id = Column(Integer, ForeignKey('users.user_id')) # сделать отдельную таблицу: id / user_id / task_id
    # performer_id = Column(Integer, ForeignKey('users.user_id'))# сделать отдельную таблицу: id / user_id / task_id

    creator = relationship(Users, foreign_keys=[creator_id])

    # watchers = relationship(Users, foreign_keys=[watcher_id])
    # performers = relationship(Users, foreign_keys=[performer_id])

    def __init__(self, creator_id, name, status=0, description=None):
        self.creator_id = creator_id
        self.name = name
        self.status = status
        self.description = description

    def __repr__(self):
        return '{} {}'.format(self.name, self.description)


if __name__ == '__main__':
    pass
