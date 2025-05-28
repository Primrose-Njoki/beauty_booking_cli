#cli/debug.py
import sys
import os


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from models.client import Client
from models.stylist import Stylist
from models.appointment import Appointment

if __name__ == '__main__':
    print("✅ Debug started successfully.")
    print(f"Client class: {Client}")
    print(f"Stylist class: {Stylist}")
    print(f"Appointment class: {Appointment}")
