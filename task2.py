"""

Task 2: Event Management System Enhancement

- Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

- Code Example: Basic Event class without participant tracking.

    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
"""

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []
        self.participant_count = 0

    def add_participant(self, participant):
        self.participants.append(participant)
        self.participant_count += 1
        print(f"Participant '{participant}' added to event.")

    def get_participant_count(self):
        print(f"\nEvent: {self.name}, Date: {self.date}, Participant Count: {self.participant_count}")
        print(f"Participants:", ', '.join(self.participants))

        
events = {}

def create_event(name, date):
    events[name] = Event(name, date)

def register_participant(event_name, participant):
    if event_name in events:
        events[event_name].add_participant(participant)

create_event('git', '08/20/2024')
register_participant('git', 'Kevin')
register_participant('git', 'Taylor')
for event in events.values():
    event.get_participant_count()