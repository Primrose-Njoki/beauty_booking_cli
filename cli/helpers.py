from models.appointment import Appointment
from datetime import timedelta
from database import Session

def check_double_booking(stylist_id, date_time, duration):
    session = Session()
    new_end = date_time + timedelta(minutes=duration)

    appointments = session.query(Appointment).filter_by(stylist_id=stylist_id).all()
    
    for appt in appointments:
        appt_end = appt.date_time + timedelta(minutes=appt.duration)
        
        if (appt.date_time <= date_time < appt_end) or (date_time <= appt.date_time < new_end):
            return True  
    return False

def print_appointments(appointments):
    if not appointments:
        print("No appointments found.")
        return
    for appt in appointments:
        print(f"ID: {appt.id} | Client ID: {appt.client_id} | Stylist ID: {appt.stylist_id} | "
              f"Service: {appt.service} | Time: {appt.date_time} | Duration: {appt.duration} mins")
