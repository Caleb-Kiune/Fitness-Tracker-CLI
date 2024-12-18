# lib/helpers.py
from models import Activity
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker()

def add_activity(session):
    activity_type = input("Enter activity type: ")
    duration = float(input("Enter duration (minutes): "))
    date_str = input("Enter date (YYYY-MM-DD): ")
    date = datetime.strptime(date_str, "%Y-%m-%d")
    details = input("Enter any additional details: ")
    
    new_activity = Activity(type=activity_type, duration=duration, date=date, details=details)
    session.add(new_activity)
    session.commit()
    print("Activity added successfully.")

def update_activity(session):
    activity_id = int(input("Enter the ID of the activity to update: "))
    activity = session.query(Activity).get(activity_id)
    if activity:
        activity.type = input(f"Enter new activity type (current: {activity.type}): ") or activity.type
        activity.duration = float(input(f"Enter new duration (current: {activity.duration}): ") or activity.duration)
        date_str = input(f"Enter new date (current: {activity.date}): ")
        activity.date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else activity.date
        activity.details = input(f"Enter new details (current: {activity.details}): ") or activity.details
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
