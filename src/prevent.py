from datetime import datetime
import tkinter as tk
from tkinter import messagebox

class Event:
    def __init__(self, event_id, capacity, date, status):
        self.event_id = event_id
        self.capacity = capacity
        self.date = date
        self.status = status
        self.registrations = []

    def display_message(self, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Registration Status", message)
        root.destroy()

    def is_full(self):
        return len(self.registrations) >= self.capacity

    def is_expired(self):
        return self.date < datetime.now()

    def is_canceled(self):
        return self.status == "canceled"

    def register_user(self, user):
        if self.is_canceled():
            self.display_message("Event has been canceled. Registration failed.")
        elif self.is_expired():
            self.display_message("Event has already expired. Registration failed.")
        elif self.is_full():
            self.display_message("Event is already full. Registration failed.")
        else:
            self.registrations.append(user)
            self.display_message("Registration successful!")

# Usage example
event = Event(event_id=1, capacity=50, date=datetime(2023, 7, 1), status="active")
user = "John Doe"  

event.register_user(user)
