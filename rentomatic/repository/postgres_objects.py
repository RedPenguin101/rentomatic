# repository/postgres_objects.py

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declatative import declarative_base

Base = delcarative_base()

class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)

    code = Column(String(36), nullable=False)
    size = Column(Integer)
    price = Column(Integer)
    longitude = Column(Float)
    latitude = Column(Float)