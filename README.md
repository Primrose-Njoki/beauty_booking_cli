# 💇‍♀️ Beauty Salon Appointment Scheduler

A command-line interface (CLI) application to manage clients, stylists, and appointments in a beauty salon. Designed for small salons that need an affordable and efficient way to schedule appointments without expensive software.


## ✅ Features

- Add, view, find, and delete clients
- Manage stylist records (create, view, delete)
- Book and manage appointments with specific services and stylists
- Prevents double-bookings and checks stylist availability
- Uses SQLAlchemy ORM with SQLite backend
- Simple CLI interface for salon staff


## 🛠 Tech Stack

- Python 3.8+**
- SQLAlchemy (ORM)
- SQLite (local database)
- CLI application (runs in terminal)


## 🗃 Data Models
Client
Stylist
Appointment

## 📁 Project Structure
beauty_booking_cli/
│
├── cli/ # CLI menus and user input
│ ├── main.py # Starts the application
│ ├── debug.py # Testing + seeding data
│ ├── client_menu.py
│ ├── stylist_menu.py
│ └── appointment_menu.py
│
├── models/ # ORM model classes
│ ├── init.py
│ ├── client.py
│ ├── stylist.py
│ └── appointment.py
│
├── database.py # Sets up engine and session
├── seed.py # Creates tables and optional test data
├── salon.db # SQLite database (generated at runtime)
└── README.md 

## Author
Primrose