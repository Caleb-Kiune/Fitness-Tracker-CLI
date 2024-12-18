# initialize_db.py
from lib.models import Base, User  
from sqlalchemy import create_engine

def initialize_database():
    engine = create_engine('sqlite:///fitness_tracker.db')
    Base.metadata.create_all(engine)
    print("Database initialized and tables created successfully.")

if __name__ == "__main__":
    initialize_database()
