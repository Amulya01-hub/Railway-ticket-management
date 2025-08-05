# Railway-ticket-management system
Create a console-based Railway Ticket Management System that allows users to create accounts, login, view trains, book tickets, and manage bookings with unique PNR generation. The system should handle user authentication, seat availability, and passenger details validation using object-oriented programming concepts.
1. Account Management
➢ Users can create new accounts with a unique username and password.
➢ Users can login using their credentials.
➢ Prevent duplicate usernames during account creation.
➢ Validate login credentials and provide appropriate success/failure messages.
2. Train Information
➢ Maintain a list of trains, each having:
● Train Number
● Source station
● Destination station
● Number of available seats
➢ Display all available trains when booking tickets
3. Ticket Booking
➢ Allow logged-in users to:
● Select a train by its number.
● Specify the number of tickets to book.
● Enter passenger details (name, age, gender, phone number) for each ticket.
➢ Validate inputs:
● Number of tickets should not exceed available seats.
● Passenger age should be within a valid range.
● Phone number must be exactly 10 digits.
➢ Generate a unique PNR number for each booked ticket.
➢ Deduct booked seats from the train's availability.
➢ Display booked ticket details including train info, passenger info, and PNR.
4. User Interface
➢ Provide a simple console menu for:
● Account creation
● Login
● Ticket booking (available only after login)
● Logout and exit
5. Data Validation
➢ Handle invalid inputs gracefully with error messages.
➢ Ensure all entered data adheres to the constraints above.
➢ Classes and Objects (Train, Passenger, Ticket, Account)
➢ Encapsulation of data and methods within classes
➢ Use of collections (lists, sets) to manage multiple objects
➢ Input validation and error handling
➢ Random number generation for unique PNRs
➢ Menu-driven program flow control
Deliverable:
A fully working console application implementing the above requirements, with clean and readable code following object-oriented programming principles.
