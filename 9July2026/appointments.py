import datetime

appointments = [
    {
        "appointment_id": 1001,
        "patient_name": "Ali Khan",
        "doctor_name": "Dr. Ahmed",
        "appointment_date": "9-07-2026",
        "appointment_time": "09:30",
        "reason": "General Checkup",
        "phone": "03001234567"
    },
    {
        "appointment_id": 1002,
        "patient_name": "Sara Malik",
        "doctor_name": "Dr. Fatima",
        "appointment_date": "18-07-2026",
        "appointment_time": "11:00",
        "reason": "Dental Consultation",
        "phone": "03111222333"
    },
    {
        "appointment_id": 1003,
        "patient_name": "Usman Raza",
        "doctor_name": "Dr. Hassan",
        "appointment_date": "21-07-2026",
        "appointment_time": "15:45",
        "reason": "Eye Examination",
        "phone": "03219876543"
    },
{
        "appointment_id": 1004,
        "patient_name": "Usman Raza 1",
        "doctor_name": "Dr. Hassan",
        "appointment_date": "09-07-2026",
        "appointment_time": "16:45",
        "reason": "Eye Examination",
        "phone": "03219876543"
    }
]

"""
1. Today's Appointments
2. Upcoming Appointments
3. Appointments This Week
"""

print("TODAY's Appointments")
for appointment in appointments:
    appointment_date = datetime.date.strptime(appointment["appointment_date"], "%d-%m-%Y")
    if appointment_date == datetime.date.today():
        print(f"Patient: {appointment["patient_name"]} - Doctor: {appointment["doctor_name"]}")


print("UPCOMING Appointments")
for appointment in appointments:
    app_date_time_str = f"{appointment["appointment_date"]} {appointment['appointment_time']}"
    app_date_time_object = datetime.datetime.strptime(app_date_time_str, "%d-%m-%Y %H:%M")
    if app_date_time_object > datetime.datetime.today() and app_date_time_object.date() == datetime.date.today():
        print(f"Patient: {appointment["patient_name"]} - Doctor: {appointment["doctor_name"]}")

print("Appointments This Week")
for appointment in appointments:
    pass

