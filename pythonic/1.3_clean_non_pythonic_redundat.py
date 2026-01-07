"""
Eliminate redondant data arguments with dataclasses
"""

from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field

# helper function to format date
def _format_date(date: str | datetime = None) -> str:
    """Return formatted date string for given datetime or now."""
    return (date or datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    
@dataclass
class Entry:
    activity: str
    duration: int
    calories_burned: int
    date: str | datetime = field(default_factory= _format_date)
    
user_name: str = "john_doe"
FITNESS_DATA_FILE = f"{user_name}_fitness_data.txt"
data_file: Path = Path(FITNESS_DATA_FILE)

def ensure_data_file(path: Path = data_file) -> None:
    header = "Date,Exercise,Duration,Calories\n"
    # Ensure parent exists (safe if using nested paths)
    if path.parent and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        f.write(header)

def add_activity(entry: Entry) -> None:
    with data_file.open("a", encoding="utf-8") as f:
        f.write(f"{entry.date},{entry.activity},{entry.duration},{entry.calories_burned}\n")
    print(f"Logged: {entry.date}, {entry.activity}, Duration: {entry.duration}, Calories: {entry.calories_burned}")

def view_logs(path: Path = data_file) -> list[str]:
    """Return list of log lines (stripped)."""
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f]


if __name__ == "__main__":
    ensure_data_file()
    add_activity(Entry("Running", 30, 300))
    add_activity(Entry("Cycling", 45, 400))
    add_activity(Entry("Swimming", 15, 250))

    print("\nExercise Logs:")
    for entry in view_logs():
        print(entry)
