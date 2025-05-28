from models.client import Client
from models.stylist import Stylist
from models.appointment import Appointment
from .helpers import check_double_booking, print_appointments
from datetime import datetime

def main_menu():
    while True:
        print("\n=== Beauty Salon Scheduler ===")
        print("1. Manage Clients")
        print("2. Manage Stylists")
        print("3. Manage Appointments")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            client_menu()
        elif choice == "2":
            stylist_menu()
        elif choice == "3":
            appointment_menu()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


def client_menu():
    while True:
        print("\n-- Clients --")
        print("1. Add Client")
        print("2. View All Clients")
        print("3. Find Client by ID")
        print("4. Delete Client")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            Client.create(name, phone, email)
            print("Client added.")
        elif choice == "2":
            for client in Client.get_all():
                print(client)
        elif choice == "3":
            id = input("Enter ID: ")
            client = Client.find_by_id(int(id))
            print(client if client else "Client not found.")
        elif choice == "4":
            id = input("Enter ID: ")
            client = Client.find_by_id(int(id))
            if client:
                client.delete()
                print("Client deleted.")
            else:
                print("Client not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def stylist_menu():
    while True:
        print("\n-- Stylists --")
        print("1. Add Stylist")
        print("2. View All Stylists")
        print("3. Find Stylist by ID")
        print("4. Delete Stylist")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            specialty = input("Specialty: ")
            Stylist.create(name, specialty)
            print("Stylist added.")
        elif choice == "2":
            for stylist in Stylist.get_all():
                print(stylist)
        elif choice == "3":
            id = input("Enter ID: ")
            stylist = Stylist.find_by_id(int(id))
            print(stylist if stylist else "Stylist not found.")
        elif choice == "4":
            id = input("Enter ID: ")
            stylist = Stylist.find_by_id(int(id))
            if stylist:
                stylist.delete()
                print("Stylist deleted.")
            else:
                print("Stylist not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def appointment_menu():
    while True:
        print("\n-- Appointments --")
        print("1. Book Appointment")
        print("2. View All Appointments")
        print("3. Find Appointment by ID")
        print("4. Cancel Appointment")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ")
        if choice == "1":
            client_id = int(input("Client ID: "))
            stylist_id = int(input("Stylist ID: "))
            service = input("Service (e.g., haircut): ")
            date_input = input("Date & time (YYYY-MM-DD HH:MM): ")
            duration = int(input("Duration in minutes: "))
            try:
                date_time = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
                if check_double_booking(stylist_id, date_time, duration):
                    print("⚠️ Stylist is not available at that time.")
                else:
                    Appointment.create(client_id, stylist_id, service, date_time, duration)
                    print("Appointment booked.")
            except ValueError:
                print("Invalid date format.")
        elif choice == "2":
            appointments = Appointment.get_all()
            print_appointments(appointments)
        elif choice == "3":
            id = input("Enter ID: ")
            appt = Appointment.find_by_id(int(id))
            print(appt if appt else "Appointment not found.")
        elif choice == "4":
            id = input("Enter ID: ")
            appt = Appointment.find_by_id(int(id))
            if appt:
                appt.delete()
                print("Appointment canceled.")
            else:
                print("Appointment not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
