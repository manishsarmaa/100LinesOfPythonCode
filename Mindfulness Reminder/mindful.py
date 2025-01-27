import time
import random

# List of mindful reminders
reminders = [
        "Take a deep breath.",
        "Stretch your body.",
        "Relax your shoulders.",
        "Close your eyes for a moment.",
        "Take a short walk.",
        "Drink some water.",
        "Smile!",
        "Think of something you're grateful for.",
        "Take a few deep breaths.",
        "Stand up and move around."
]

# Function to display reminders
def send_reminder():
    reminder = random.choice(reminders)
    print(f"Mindful Moment: {reminder}")

# Schedule reminders
def start_reminders(interval_minutes=30):
    print("Welcome to the Mindful Moments App! 🌼")
    try:
        while True:
            send_reminder()
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds
    except KeyboardInterrupt:
        print("\nStopping reminders. Stay mindful!")

# Start reminders with a 30-minute interval
start_reminders(interval_minutes=30)
