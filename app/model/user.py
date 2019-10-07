from sqlalchemy import Column, Index, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT

from .. import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(INTEGER(10), primary_key=True)
    email = Column(String(191), nullable=False)
    password = Column(String(191), nullable=False)
    username = Column(String(191), nullable=False)
    level = Column(TINYINT(4), nullable=False)
