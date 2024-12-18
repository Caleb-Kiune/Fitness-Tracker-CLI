from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.orm import relationship
from .base import Base

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    type = Column(String)
    duration = Column(Float)
    date = Column(Date)
    details = Column(String)
