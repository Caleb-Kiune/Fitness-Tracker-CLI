# lib/helpers.py
from models import User, Goal, Activity
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Session = sessionmaker()

def add_activity(session):

    # dictionary used to store activity details
    activity_data = {
        'type': input("Enter activity type: ").strip(),
    }
    
    if not activity_data['type']:
        print("Error: Activity type cannot be empty.")
        return

    try:
        activity_data['duration'] = float(input("Enter duration (minutes): "))
        if activity_data['duration'] <= 0:
            print("Error: Duration must be a positive number.")
            return
    except ValueError:
        print("Error: Duration must be a number.")
        return

    date_str = input("Enter date (DD-MM-YYYY): ")
    try:
        activity_data['date'] = datetime.strptime(date_str, "%d-%m-%Y")
    except ValueError:
        print("Error: Date must be in DD-MM-YYYY format.")
        return

    activity_data['details'] = input("Enter any additional details: ").strip()

    # Activity object using the dictionary
    new_activity = Activity(**activity_data)
    session.add(new_activity)
    session.commit()
    print("Activity added successfully.")


def update_activity(session):
    activity_id = int(input("Enter the ID of the activity to update: "))
    activity = session.query(Activity).get(activity_id)
    if activity:

        # tuple used to store activity details
        current_details = (activity.type, activity.duration, activity.date, activity.details)
        
        new_type = input(f"Enter new activity type (current: {current_details[0]}): ").strip() or current_details[0]
        if not new_type:
            print("Error: Activity type cannot be empty.")
            return
        
        duration_str = input(f"Enter new duration (current: {current_details[1]}): ").strip()
        duration = float(duration_str) if duration_str else current_details[1]
        if duration <= 0:
            print("Error: Duration must be a positive number.")
            return
        
        date_str = input(f"Enter new date (current: {current_details[2]}): ").strip()
        date = datetime.strptime(date_str, "%d-%m-%Y") if date_str else current_details[2]
        
        new_details = input(f"Enter new details (current: {current_details[3]}): ").strip() or current_details[3]
        
        activity.type = new_type
        activity.duration = duration
        activity.date = date
        activity.details = new_details
        
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

    #use of list to collect activity information
    activity_list = []
    for activity in activities:
        activity_info = {
            'ID': activity.id,
            'Type': activity.type,
            'Duration': activity.duration,
            'Date': activity.date,
            'Details': activity.details
        }
        activity_list.append(activity_info)
        print(f"ID: {activity.id}, Type: {activity.type}, Duration: {activity.duration}, Date: {activity.date}, Details: {activity.details}")
    return activity_list


def add_user(session):
    name = input("Enter user name: ").strip()
    email = input("Enter user email: ").strip()
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    print("User added successfully.")

def view_users(session):
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    return users

def delete_user(session):
    user_id = int(input("Enter the ID of the user to delete: "))
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully.")
    else:
        print("User not found.")


def add_goal(session):
    user_id = int(input("Enter user ID: ").strip())
    target_type = input("Enter target type (e.g., distance, time): ").strip()
    target_value = float(input("Enter target value: "))
    deadline_str = input("Enter deadline (DD-MM-YYYY): ").strip()
    deadline = datetime.strptime(deadline_str, "%d-%m-%Y")
    new_goal = Goal(user_id=user_id, target_type=target_type, target_value=target_value, deadline=deadline)
    session.add(new_goal)
    session.commit()
    print("Goal added successfully.")


def view_goals(session):
    goals = session.query(Goal).all()
    for goal in goals:
        print(f"ID: {goal.id}, User ID: {goal.user_id}, Target Type: {goal.target_type}, Target Value: {goal.target_value}, Deadline: {goal.deadline}")
    return goals


def delete_goal(session):
    goal_id = int(input("Enter the ID of the goal to delete: "))
    goal = session.query(Goal).get(goal_id)
    if goal:
        session.delete(goal)
        session.commit()
        print("Goal deleted successfully.")
    else:
        print("Goal not found.")








