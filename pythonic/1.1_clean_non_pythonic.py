# Removing unnecessary classes and simplifying the code structure for better readability and maintainability.
# There are not variables in class
# We dont need multimple instances of this class
# We can use functions instead of class methods for this simple functionality
# Remove the self parameter from methods, the init method and class definition, the class prefix from method calls
# Cleaned up version of a simple fitness tracker application

import os
from datetime import datetime

user_name = "john_doe"
data_file = f"{user_name}_fitness_data.txt"

def ensure_data_file():
    with open(data_file, 'w') as f:
        f.write("Date,Exercise,Duration (minutes),Calories Burned\n")

def log_activity( activity, calories_burned, date=None):
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(data_file, 'a') as f:
        f.write(f"{date},{activity},{calories_burned}\n")
        print(f"Logged: {activity} on {date}, Calories Burned: {calories_burned}")
    
def log_exercise( exercise, duration, calories):
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(data_file, 'a') as f:
        f.write(f"{date_str},{exercise},{duration},{calories}\n")
        print(f"Logged: {exercise} for {duration} minutes, {calories} calories burned.")

def view_logs():
    with open(data_file, 'r') as f:
        logs = f.readlines()
        for log in logs:
            print(log.strip())
            
            
if __name__ == "__main__":
    ensure_data_file()
    log_exercise("Running", 30, 300)
    log_exercise("Cycling", 45, 400)
    log_activity("Swimming", 250)
    
    print("\nExercise Logs:")
    view_logs()
    

    
    