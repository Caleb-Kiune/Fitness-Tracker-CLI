from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Goal(Base):
    __tablename__ = 'goals'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    target_type = Column(String, nullable=False)
    target_value = Column(Float, nullable=False)
    deadline = Column(Date, nullable=False)

    user = relationship('User', back_populates='goals') 
