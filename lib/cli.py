# lib/cli.py
from helpers import add_activity, update_activity, delete_activity, view_activities, add_user
from sqlalchemy.orm import sessionmaker
from lib.models import Base, User  # Only import User
from sqlalchemy import create_engine

def main():
    engine = create_engine('sqlite:///fitness_tracker.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("1. Add New Activity")
        print("2. Update Existing Activity")
        print("3. Delete an Activity")
        print("4. View All Activities")
        print("5. Add New User")
        print("6. Exit")
        
        choice = input("> ")
        if choice == "1":
            add_activity(session)
        elif choice == "2":
            update_activity(session)
        elif choice == "3":
            delete_activity(session)
        elif choice == "4":
            view_activities(session)
        elif choice == "5":
            add_user(session)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
