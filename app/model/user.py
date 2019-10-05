from sqlalchemy import Column, Index, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT

from .. import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = (Index('email', 'email', 'username', unique=True), )

    id = Column(INTEGER(10), primary_key=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    level = Column(TINYINT(4), nullable=False)
