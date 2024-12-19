# lib/cli.py
from helpers import add_activity, update_activity, delete_activity, view_activities, add_user, view_users, delete_user, add_goal, view_goals, delete_goal
from sqlalchemy.orm import sessionmaker
from models import Base, Activity, User, Goal
from sqlalchemy import create_engine

def main():
    engine = create_engine('sqlite:///fitness_tracker.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("1. Add New User")
        print("2. View All Users")
        print("3. Delete a User")
        print("4. Add New Activity")
        print("5. Update Existing Activity")
        print("6. Delete an Activity")
        print("7. View All Activities")
        print("8. Add New Goal")
        print("9. View All Goals")
        print("10. Delete a Goal")
        print("11. Exit")
        
        choice = input("> ")
        if choice == "1":
            add_user(session)
        elif choice == "2":
            view_users(session)
        elif choice == "3":
            delete_user(session)
        elif choice == "4":
            add_activity(session)
        elif choice == "5":
            update_activity(session)
        elif choice == "6":
            delete_activity(session)
        elif choice == "7":
            view_activities(session)
        elif choice == "8":
            add_goal(session)
        elif choice == "9":
            view_goals(session)
        elif choice == "10":
            delete_goal(session)
        elif choice == "11":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
