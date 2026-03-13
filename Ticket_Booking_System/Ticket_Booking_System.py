# -------------------------------
# Ticket Booking System (DSA Project)
# Data Structures Used:
# Array -> Seats
# Queue -> Waiting List
# Stack -> Cancellation History
# Searching -> Find booking
# -------------------------------

TOTAL_SEATS = 10

# Array for seats
seats = [0] * TOTAL_SEATS

# Dictionary to store booking details
bookings = {}

# Queue for waiting list
waiting_list = []

# Stack for cancellation history
cancel_stack = []


# -------------------------------
# Book Ticket
# -------------------------------
def book_ticket():
    name = input("Enter your name: ")

    for i in range(TOTAL_SEATS):
        if seats[i] == 0:
            seats[i] = 1
            bookings[i + 1] = name
            print(f"Ticket booked successfully! Seat Number: {i+1}")
            return

    print("All seats are booked!")
    print("Added to waiting list.")
    waiting_list.append(name)


# -------------------------------
# Cancel Ticket
# -------------------------------
def cancel_ticket():
    seat_no = int(input("Enter seat number to cancel: "))

    if seat_no in bookings:
        name = bookings.pop(seat_no)
        seats[seat_no - 1] = 0

        cancel_stack.append(seat_no)

        print(f"Ticket for {name} cancelled successfully.")

        if waiting_list:
            new_person = waiting_list.pop(0)
            seats[seat_no - 1] = 1
            bookings[seat_no] = new_person
            print(f"Seat given to waiting person: {new_person}")

    else:
        print("Invalid seat number or not booked.")


# -------------------------------
# Show Available Seats
# -------------------------------
def show_seats():
    print("\nAvailable Seats:")

    available = False
    for i in range(TOTAL_SEATS):
        if seats[i] == 0:
            print(i + 1, end=" ")
            available = True

    if not available:
        print("No seats available")

    print()


# -------------------------------
# Show Bookings
# -------------------------------
def show_bookings():
    if not bookings:
        print("No bookings yet.")
        return

    print("\nBooking Details:")
    for seat, name in bookings.items():
        print(f"Seat {seat} -> {name}")


# -------------------------------
# Show Waiting List
# -------------------------------
def show_waiting_list():
    if not waiting_list:
        print("Waiting list is empty.")
    else:
        print("Waiting List:")
        for person in waiting_list:
            print(person)


# -------------------------------
# Search Booking
# -------------------------------
def search_booking():
    name = input("Enter name to search booking: ")

    for seat, person in bookings.items():
        if person.lower() == name.lower():
            print(f"{name} has booked Seat {seat}")
            return

    print("Booking not found.")


# -------------------------------
# Show Cancellation History
# -------------------------------
def show_cancellations():
    if not cancel_stack:
        print("No cancellations yet.")
    else:
        print("Cancellation History (Stack):")
        for seat in reversed(cancel_stack):
            print(f"Seat {seat}")


# -------------------------------
# Main Menu
# -------------------------------
while True:

    print("\n------ Ticket Booking System ------")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Show Available Seats")
    print("4. Show Booking Details")
    print("5. Show Waiting List")
    print("6. Search Booking")
    print("7. Show Cancellation History")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_ticket()

    elif choice == "2":
        cancel_ticket()

    elif choice == "3":
        show_seats()

    elif choice == "4":
        show_bookings()

    elif choice == "5":
        show_waiting_list()

    elif choice == "6":
        search_booking()

    elif choice == "7":
        show_cancellations()

    elif choice == "8":
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice. Try again.")