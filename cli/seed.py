from database import Base, engine, Session
from models.client import Client
from models.stylist import Stylist
from models.appointment import Appointment
from datetime import datetime, timedelta

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()

c1 = Client(name="Alice Johnson", phone="123-456-7890", email="alice@example.com")
c2 = Client(name="Bob Smith", phone="987-654-3210", email="bob@example.com")

s1 = Stylist(name="Maya Lee", specialty="Haircut")
s2 = Stylist(name="Daniel Ray", specialty="Manicure")

a1 = Appointment(client=c1, stylist=s1, service="Haircut", date_time=datetime(2025, 5, 28, 10, 0), duration=30)
a2 = Appointment(client=c2, stylist=s2, service="Manicure", date_time=datetime(2025, 5, 28, 11, 0), duration=45)

session.add_all([c1, c2, s1, s2, a1, a2])
session.commit()

print("✅ Database seeded with sample data.")
