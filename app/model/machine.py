from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMINT, SMALLINT
from sqlalchemy.orm import relationship

from .. import db


class Machine(db.Model):
    __tablename__ = 'machine'

    id = Column(INTEGER(10), primary_key=True)
    user_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    port = Column(SMALLINT(5), nullable=False, unique=True)
    cpu = Column(Float, nullable=False)
    memory = Column(MEDIUMINT(8), nullable=False)

    user = relationship('User')
