import datetime

events = [
    {
        "name": "Python Bootcamp",
        "start_date": datetime.date(2026, 9, 1),
        "end_date": datetime.date(2026, 9, 2)
    },
    {
        "name": "Database Workshop",
        "start_date": datetime.date(2026, 9, 8),
        "end_date": datetime.date(2026, 9, 10)
    }
]

# Take an event from user. Event name, start date and end date.
# Add event into the list
# Give an error message if the slot is booked already.

user_event_name = "New Event"
user_event_start_date = "10/September/2026"
user_event_start_date = datetime.date.strptime(user_event_start_date, "%d/%B/%Y")
user_event_end_date = "11/September/2026"
user_event_end_date = datetime.date.strptime(user_event_end_date, "%d/%B/%Y")

print(user_event_name, user_event_start_date, user_event_end_date)
print("==============")

overlap = False
for event in events:
    if user_event_start_date >= event["start_date"] and user_event_start_date <= event["end_date"]:
        print(f"overlapping with {event['name']} start issue")
        overlap = True
        break
    if user_event_end_date >= event["start_date"] and user_event_end_date <= event["end_date"]:
        print(f"overlapping with {event['name']}: ending issue")
        overlap = True
        break

if overlap:
    print(f"not available")
else:
    print(f"available")
