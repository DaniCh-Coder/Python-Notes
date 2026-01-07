# Non pythonic version of a simple fitness tracker application
import os
from datetime import datetime

class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.data_file = f"{user_name}_fitness_data.txt"
        self.ensure_data_file()

    def ensure_data_file(self):
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                f.write("Date,Exercise,Duration (minutes),Calories Burned\n")

    def log_activity(self, activity, calories_burned, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.data_file, 'a') as f:
            f.write(f"{date},{activity},{calories_burned}\n")
        print(f"Logged: {activity} on {date}, Calories Burned: {calories_burned}")
        
    def log_exercise(self, exercise, duration, calories):
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.data_file, 'a') as f:
            f.write(f"{date_str},{exercise},{duration},{calories}\n")
        print(f"Logged: {exercise} for {duration} minutes, {calories} calories burned.")

    def view_logs(self):
        with open(self.data_file, 'r') as f:
            logs = f.readlines()
        for log in logs:
            print(log.strip())
            
            
if __name__ == "__main__":
    tracker = FitnessTracker("john_doe")
    tracker.log_exercise("Running", 30, 300)
    tracker.log_exercise("Cycling", 45, 400)
    tracker.log_activity("Swimming", 250)
    
    print("\nExercise Logs:")
    tracker.view_logs()
    

    
    