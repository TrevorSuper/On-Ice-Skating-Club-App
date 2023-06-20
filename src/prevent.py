from datetime import datetime

class Event:
    def __init__(self, event_id, capacity, date, status):
        self.event_id = event_id
        self.capacity = capacity
        self.date = date
        self.status = status
        self.registrations = []

    def is_full(self):
        return len(self.registrations) >= self.capacity

    def is_expired(self):
        return self.date < datetime.now()

    def is_canceled(self):
        return self.status == "canceled"

    def register_user(self, user):
        if self.is_canceled():
            return "Event has been canceled. Registration failed."
        elif self.is_expired():
            return "Event has already expired. Registration failed."
        elif self.is_full():
            return "Event is already full. Registration failed."
        else:
            self.registrations.append(user)
            return "Registration Unsuccessful Due to the Event already EXPIRED, FULL, or CANCELLED!"

# Usage example
event = Event(event_id=1, capacity=50, date=datetime(2023, 7, 1), status="active")
user = "John Doe"  # Assuming you have a User class or simply using a string for demonstration

registration_result = event.register_user(user)
print(registration_result)

