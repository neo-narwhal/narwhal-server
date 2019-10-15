from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT

from .. import db

from app import ph


class User(db.Model):
    __tablename__ = 'user'

    id = Column(INTEGER(10), primary_key=True)
    email = Column(String(191), nullable=False)
    password = Column(String(191), nullable=False)
    username = Column(String(191), nullable=False)
    level = Column(TINYINT(4), nullable=False)

    def check_password(self, password):
        return ph.verify(self.password, password)

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}