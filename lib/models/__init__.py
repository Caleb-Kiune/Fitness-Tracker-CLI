from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .activity import Activity
from .user import User
from .goal import Goal
