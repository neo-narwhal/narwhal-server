from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship

from .. import db


class Addon(db.Model):
    __tablename__ = 'addon'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(191), nullable=False, unique=True)
    project_id = Column(ForeignKey('project.id'), nullable=False, index=True)

    project = relationship('Project')
