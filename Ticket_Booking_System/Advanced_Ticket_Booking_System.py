import tkinter as tk
from tkinter import messagebox

TOTAL_SEATS = 10

seats = [0] * TOTAL_SEATS
bookings = {}
waiting_list = []
cancel_stack = []

# -----------------------------
# Book Ticket
# -----------------------------
def book_ticket(seat_no):
    name = name_entry.get()

    if name == "":
        messagebox.showwarning("Error", "Please enter your name")
        return

    if seats[seat_no] == 0:
        seats[seat_no] = 1
        bookings[seat_no + 1] = name
        seat_buttons[seat_no].config(bg="red", text=f"{seat_no+1}\nBooked")

        messagebox.showinfo("Success", f"Seat {seat_no+1} booked for {name}")
        name_entry.delete(0, tk.END)

    else:
        waiting_list.append(name)
        messagebox.showinfo("Waiting List", "Seat already booked. Added to waiting list.")


# -----------------------------
# Cancel Ticket
# -----------------------------
def cancel_ticket():
    seat_no = seat_entry.get()

    if seat_no == "":
        messagebox.showwarning("Error", "Enter seat number")
        return

    seat_no = int(seat_no)

    if seat_no in bookings:

        name = bookings.pop(seat_no)
        seats[seat_no - 1] = 0
        cancel_stack.append(seat_no)

        seat_buttons[seat_no-1].config(bg="green", text=str(seat_no))

        messagebox.showinfo("Cancelled", f"Seat {seat_no} cancelled")

        if waiting_list:
            new_person = waiting_list.pop(0)
            bookings[seat_no] = new_person
            seats[seat_no - 1] = 1
            seat_buttons[seat_no-1].config(bg="red", text=f"{seat_no}\nBooked")
            messagebox.showinfo("Waiting List", f"Seat given to {new_person}")

    else:
        messagebox.showerror("Error", "Seat not booked")

    seat_entry.delete(0, tk.END)


# -----------------------------
# Search Booking
# -----------------------------
def search_booking():
    name = search_entry.get()

    for seat, person in bookings.items():
        if person.lower() == name.lower():
            messagebox.showinfo("Found", f"{name} booked Seat {seat}")
            return

    messagebox.showinfo("Result", "Booking not found")


# -----------------------------
# Show Waiting List
# -----------------------------
def show_waiting():
    if not waiting_list:
        messagebox.showinfo("Waiting List", "No one waiting")
    else:
        messagebox.showinfo("Waiting List", "\n".join(waiting_list))


# -----------------------------
# GUI Window
# -----------------------------
root = tk.Tk()
root.title("Ticket Booking System")
root.geometry("600x600")
root.config(bg="#1e1e2f")

title = tk.Label(
    root,
    text="Ticket Booking System",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e2f"
)
title.pack(pady=10)


# -----------------------------
# Name Input
# -----------------------------
tk.Label(root, text="Enter Name", fg="white", bg="#1e1e2f").pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)


# -----------------------------
# Seat Layout (Cinema Style)
# -----------------------------
seat_frame = tk.Frame(root, bg="#1e1e2f")
seat_frame.pack(pady=20)

seat_buttons = []

for i in range(TOTAL_SEATS):

    btn = tk.Button(
        seat_frame,
        text=str(i+1),
        width=8,
        height=3,
        bg="green",
        command=lambda i=i: book_ticket(i)
    )

    btn.grid(row=i//5, column=i%5, padx=10, pady=10)

    seat_buttons.append(btn)


# -----------------------------
# Cancel Section
# -----------------------------
tk.Label(root, text="Cancel Seat Number", fg="white", bg="#1e1e2f").pack()

seat_entry = tk.Entry(root)
seat_entry.pack()

tk.Button(
    root,
    text="Cancel Ticket",
    command=cancel_ticket,
    bg="orange",
    width=20
).pack(pady=5)


# -----------------------------
# Search Section
# -----------------------------
tk.Label(root, text="Search Booking (Name)", fg="white", bg="#1e1e2f").pack()

search_entry = tk.Entry(root)
search_entry.pack()

tk.Button(
    root,
    text="Search Booking",
    command=search_booking,
    bg="cyan",
    width=20
).pack(pady=5)


# -----------------------------
# Waiting List Button
# -----------------------------
tk.Button(
    root,
    text="Show Waiting List",
    command=show_waiting,
    bg="yellow",
    width=20
).pack(pady=10)


root.mainloop()