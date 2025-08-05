import random
import os
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bookings = []  
class Train:
    def __init__(self, train_number, source, destination, total_seats):
        self.train_number = train_number
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
class Booking:
    def __init__(self, pnr, train, passenger_details):
        self.pnr = pnr
        self.train = train
        self.passenger_details = passenger_details
class RailwayTicketManagementSystem:
    def __init__(self):
        self.users = {}  
        self.trains = [
            Train("T101", "Delhi", "Mumbai", 100),
            Train("T102", "Mumbai", "Chennai", 75),
            Train("T103", "Chennai", "Kolkata", 120),
            Train("T104", "Kolkata", "Delhi", 90)
        ]
        self.current_user = None
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def create_account(self):
        self.clear_screen()
        print("----- Create Account -----")
        while True:
            username = input("Enter a unique username: ")
            if username in self.users:
                print("Username already exists. Please choose a different one.")
            else:
                break
        password = input("Enter a password: ")
        self.users[username] = User(username, password)
        print("Account created successfully!")
        input("Press Enter to continue...")
    def login(self):
        """Allows a user to log in."""
        self.clear_screen()
        print("----- Login -----")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user = self.users.get(username)
        if user and user.password == password:
            self.current_user = user
            print("Login successful!")
        else:
            print("Invalid username or password.")
        input("Press Enter to continue...")
    def logout(self):
        if self.current_user:
            self.current_user = None
            print("Logged out successfully.")
        else:
            print("No user is currently logged in.")
        input("Press Enter to continue...")
    def display_trains(self):
        self.clear_screen()
        print("----- Available Trains -----")
        print("{:<15} {:<15} {:<15} {:<15}".format("Train No.", "Source", "Destination", "Available Seats"))
        print("-" * 60)
        for train in self.trains:
            print("{:<15} {:<15} {:<15} {:<15}".format(train.train_number, train.source, train.destination, train.available_seats))
        print("-" * 60)
        input("Press Enter to continue...")
    def book_ticket(self):
        if not self.current_user:
            print("Please log in to book a ticket.")
            input("Press Enter to continue...")
            return
        self.clear_screen()
        print("----- Book a Ticket -----")
        self.display_trains()
        train_number = input("Enter the train number you wish to book: ").upper()
        selected_train = next((t for t in self.trains if t.train_number == train_number), None)
        if not selected_train:
            print("Invalid train number.")
            input("Press Enter to continue...")
            return
        try:
            num_tickets = int(input("Enter the number of tickets to book: "))
            if num_tickets <= 0:
                raise ValueError
        except ValueError:
            print("Invalid number of tickets. Please enter a positive integer.")
            input("Press Enter to continue...")
            return
        if num_tickets > selected_train.available_seats:
            print(f"Sorry, only {selected_train.available_seats} seats are available.")
            input("Press Enter to continue...")
            return
        passengers = []
        print("\nEnter Passenger Details:")
        for i in range(num_tickets):
            print(f"--- Passenger {i + 1} ---")
            name = input("Name: ")
            while True:
                try:
                    age = int(input("Age: "))
                    if 1 <= age <= 100:
                        break
                    else:
                        print("Invalid age. Please enter an age between 1 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid age (a number).")
            gender = input("Gender (M/F/O): ").upper()
            while gender not in ['M', 'F', 'O']:
                gender = input("Invalid gender. Please enter M, F, or O: ").upper()
            while True:
                phone = input("Phone Number (10 digits): ")
                if phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print("Invalid phone number. It must be exactly 10 digits.")
            passengers.append({'name': name, 'age': age, 'gender': gender, 'phone': phone})
        pnr = f"PNR{random.randint(100000, 999999)}"
        new_booking = Booking(pnr, selected_train, passengers)
        self.current_user.bookings.append(new_booking)
        selected_train.available_seats -= num_tickets 
        print("\n--- Ticket Booked Successfully! ---")
        self.display_ticket(new_booking)
        input("Press Enter to continue...")
    def display_ticket(self, booking):
        self.clear_screen()
        print("----- Your E-Ticket -----")
        print(f"PNR Number: {booking.pnr}")
        print(f"Train Number: {booking.train.train_number}")
        print(f"Route: {booking.train.source} -> {booking.train.destination}")
        print("\nPassenger Details:")
        for i, p in enumerate(booking.passenger_details):
            print(f"  {i+1}. Name: {p['name']}, Age: {p['age']}, Gender: {p['gender']}, Phone: {p['phone']}")
        print("-" * 60)
    def main_menu(self):
        while True:
            self.clear_screen()
            print("="*40)
            print("  Railway Ticket Management System  ")
            print("="*40)
            if self.current_user:
                print(f"Welcome, {self.current_user.username}!")
                print("1. Book a Ticket")
                print("2. View Bookings")
                print("3. Logout")
            else:
                print("1. Create Account")
                print("2. Login")
                print("3. Exit")
            print("="*40) 
            choice = input("Enter your choice: ")
            if self.current_user:
                if choice == '1':
                    self.book_ticket()
                elif choice == '2':
                    self.view_bookings()
                elif choice == '3':
                    self.logout()
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
            else:
                if choice == '1':
                    self.create_account()
                elif choice == '2':
                    self.login()
                elif choice == '3':
                    print("Thank you for using the system. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
    def view_bookings(self):
        if not self.current_user:
            print("Please log in to view your bookings.")
            input("Press Enter to continue...")
            return
        self.clear_screen()
        print(f"----- Bookings for {self.current_user.username} -----")
        if not self.current_user.bookings:
            print("You have no bookings yet.")
        else:
            for booking in self.current_user.bookings:
                self.display_ticket(booking)
                print("\n" + "="*60 + "\n")
        input("Press Enter to continue...")
system = RailwayTicketManagementSystem()
system.main_menu()
