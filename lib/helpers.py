from models import Activity
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker()

def add_activity(session):
    activity_type = input("Enter activity type: ").strip()
    if not activity_type:
        print("Error: Activity type cannot be empty.")
        return
    
    try:
        duration = float(input("Enter duration (minutes): "))
        if duration <= 0:
            print("Error: Duration must be a positive number.")
            return
    except ValueError:
        print("Error: Duration must be a number.")
        return
    
    date_str = input("Enter date (DD-MM-YYYY): ")
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Error: Date must be in DD-MM-YYYY format.")
        return
    
    details = input("Enter any additional details: ").strip()
    new_activity = Activity(type=activity_type, duration=duration, date=date, details=details)
    session.add(new_activity)
    session.commit()
    print("Activity added successfully.")

# lib/helpers.py
def update_activity(session):
    activity_id = int(input("Enter the ID of the activity to update: "))
    activity = session.query(Activity).get(activity_id)
    if activity:
        activity_type = input(f"Enter new activity type (current: {activity.type}): ").strip() or activity.type
        if not activity_type:
            print("Error: Activity type cannot be empty.")
            return
        
        duration_str = input(f"Enter new duration (current: {activity.duration}): ").strip()
        if duration_str:
            try:
                duration = float(duration_str)
                if duration <= 0:
                    print("Error: Duration must be a positive number.")
                    return
                activity.duration = duration
            except ValueError:
                print("Error: Duration must be a number.")
                return
        
        date_str = input(f"Enter new date (current: {activity.date}): ").strip()
        if date_str:
            try:
                activity.date = datetime.strptime(date_str, "%d-%m-%Y")
            except ValueError:
                print("Error: Date must be in DD-MM-YYYY format.")
                return
        
        activity.details = input(f"Enter new details (current: {activity.details}): ").strip() or activity.details
        session.commit()
        print("Activity updated successfully.")
    else:
        print("Activity not found.")


def delete_activity(session):
    activity_id = int(input("Enter the ID of the activity to delete: "))
    activity = session.query(Activity).get(activity_id)
    if activity:
        session.delete(activity)
        session.commit()
        print("Activity deleted successfully.")
    else:
        print("Activity not found.")

def view_activities(session):
    activities = session.query(Activity).all()
    for activity in activities:
        print(f"ID: {activity.id}, Type: {activity.type}, Duration: {activity.duration}, Date: {activity.date}, Details: {activity.details}")
