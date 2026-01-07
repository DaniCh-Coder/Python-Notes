"""
Simple fitness logging with improved type annotations.
"""

from datetime import datetime
from pathlib import Path


user_name: str = "john_doe"
data_file: Path = Path(f"{user_name}_fitness_data.txt")


def ensure_data_file(path: Path = data_file) -> None:
    header = "Date,Exercise,Duration (minutes),Calories Burned\n"
    # Ensure parent exists (safe if using nested paths)
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(header)


def _format_date(date: str | datetime) -> str:
    """Return formatted date string for given datetime or now."""
    return (date or datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


def log_activity(activity: str, duration: int, calories_burned: int, date: str | datetime = None) -> None:
    date_str = _format_date(date)
    with data_file.open("a", encoding="utf-8") as f:
        f.write(f"{date_str},{activity},{duration},{calories_burned}\n")
    print(f"Logged: {activity} on {date_str}, Calories Burned: {calories_burned}")


def log_exercise(exercise: str, duration: int, calories: int, date: str | datetime = None) -> None:
    # Delegate to log_activity to keep behavior consistent
    log_activity(exercise, duration, calories, date)


def view_logs(path: Path = data_file) -> list[str]:
    """Return list of log lines (stripped)."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f]


if __name__ == "__main__":
    ensure_data_file()
    log_exercise("Running", 30, 300)
    log_exercise("Cycling", 45, 400)
    log_activity("Swimming", 15, 250)

    print("\nExercise Logs:")
    for entry in view_logs():
        print(entry)
