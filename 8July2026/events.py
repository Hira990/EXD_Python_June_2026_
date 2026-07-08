from datetime import datetime

events = [
    {
        "name": "Python Bootcamp",
        "start_date": datetime(2025, 9, 1, 9, 0),
        "end_date": datetime(2025, 9, 1, 17, 0)
    },
    {
        "name": "Database Workshop",
        "start_date": datetime(2025, 9, 3, 10, 30),
        "end_date": datetime(2025, 9, 3, 15, 30)
    },
    {
        "name": "Team Meeting",
        "start_date": datetime(2025, 9, 5, 14, 0),
        "end_date": datetime(2025, 9, 5, 15, 30)
    },
    {
        "name": "Hackathon",
        "start_date": datetime(2025, 9, 7, 8, 0),
        "end_date": datetime(2025, 9, 8, 20, 0)
    },
    {
        "name": "Project Presentation",
        "start_date": datetime(2025, 9, 10, 13, 0),
        "end_date": datetime(2025, 9, 10, 15, 0)
    },
    {
        "name": "Networking Event",
        "start_date": datetime(2025, 9, 12, 18, 0),
        "end_date": datetime(2025, 9, 12, 21, 0)
    },
    {
        "name": "Machine Learning Seminar",
        "start_date": datetime(2025, 9, 15, 9, 30),
        "end_date": datetime(2025, 9, 15, 12, 30)
    },
    {
        "name": "Coding Competition",
        "start_date": datetime(2025, 9, 18, 10, 0),
        "end_date": datetime(2025, 9, 18, 16, 0)
    },
    {
        "name": "Client Meeting",
        "start_date": datetime(2025, 9, 22, 11, 0),
        "end_date": datetime(2025, 9, 22, 12, 30)
    },
    {
        "name": "Final Exam",
        "start_date": datetime(2025, 9, 30, 9, 0),
        "end_date": datetime(2025, 9, 30, 12, 0)
    }
]

# Take an event from user. Event name, start date and end date.
# Add event into the list
# Give an error message if the slot is booked already.