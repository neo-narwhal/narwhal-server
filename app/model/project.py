from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship

from .. import db


class Project(db.Model):
    __tablename__ = 'project'

    id = Column(INTEGER(10), primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    name = Column(String(191), nullable=False, unique=True)
    port = Column(TINYINT(4), nullable=False)
    type = Column(String(191), nullable=False)
    status = Column(String(191), nullable=False)

    user = relationship('User')
