from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from .. import db


class Project(db.Model):
    __tablename__ = 'project'

    id = Column(INTEGER(10), primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    name = Column(String(191), nullable=False)
    description = Column(String(191), nullable=False)
    image_tag = Column(String(191), nullable=False)

    user = relationship('User')
