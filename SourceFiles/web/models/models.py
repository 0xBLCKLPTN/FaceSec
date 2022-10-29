from sqlalchemy import Column, String, Integer, DateTime
from db.db import Base
from datetime import datetime


class UnknownFace(Base):
    __tablename__ = 'UnknownFaceLog'

    id = Column(Integer, primary_key=True)
    path_to_face = Column(String)
    created = Column(DateTime, default=datetime.utcnow)
    status = Column(String)


class KnownFaces(Base):
    __tablename__ = 'KnownFaces'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    second_name = Column(String)
    path_to_face = Column(String)
    face_token = Column(String)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)
