# -*- coding: utf-8 -*-
"""Witter.Larhone-PythonCode-ITT103-F2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jq1RF0xSRvRMtBck1mQnM_IqNR6H0N5I
"""

#Author: Larhone Witter
#Date Created: December 19,2023
#Course: ITT103
#Purpose: This program will reserve seat in a bus class of your choice it allows you to selected window or aisle and also gives you the option to quit at anytime.

# Constants representing seat capacities
F_CLASS_CAP = 27  # Constant for class capacities for First Class
B_CLASS_CAP = 38  # Constant for class capacities for Business Class
E_CLASS_CAP = 56  # Constant for class capacities for Economy Class

# Initializing seat arrays for each class
f_class_seats = [['Available' for _ in range(6)] for _ in range(5)]  # Represents a 5x6 seating arrangement for First Class
b_class_seats = [['Available' for _ in range(6)] for _ in range(7)]  # Represents a 7x6 seating arrangement for Business Class
e_class_seats = [['Available' for _ in range(7)] for _ in range(8)]  # Represents an 8x7 seating arrangement for Economy Class

# Function to display the reservation options menu
#modifcation in defining a function
def passenger_menu():
    print("UCC Signature Express Limited")
    print("<ROUTE TO STUDENTS SUCCESS VIA COMMONWEALTH MINDS>")
    print("Reservation Options:")
    print(" First Class (F/f)")
    print(" Business Class (B/b)")
    print(" Economy Class (E/e)")
    print(" Quit or Cancel (Q/q)")
    print("Please select an option:")

# Function to reserve a seat
def reserve_seat(seat_opt, travel_class_type):

    pasnger_row_number = int(input("Enter the row number in the bus (integer): "))

    pasnger_seat_type = int(input("Indicate your seat type 1 for Window or 2 for Aisle: "))
# modification with nested if
    if pasnger_seat_type == 1:
        pasnger_seat_column = 1  # Assign window seat
    elif pasnger_seat_type == 2:
        pasnger_seat_column = len(seat_opt[pasnger_row_number - 1])  # Assign aisle seat
    else:
        print("Please enter a valid seat type!")
        print("\n")
        passenger_menu()
        return

    if pasnger_row_number <= 0:
        print("Number must be positive or greater than zero!")
        print("\n")
    elif pasnger_row_number > len(seat_opt) or pasnger_seat_column > len(seat_opt[0]):
        print("Seat does not exist. Please choose a valid seat.")
        print("\n")
    else:
        if seat_opt[pasnger_row_number - 1][pasnger_seat_column - 1] == 'Reserved':
            print("Seat already taken. Please choose another seat.")
            print("\n")
        else:
            seat_opt[pasnger_row_number - 1][pasnger_seat_column - 1] = 'Reserved'
            if pasnger_row_number == 10 and pasnger_seat_column == 1:
                print("Reserving seat: row 10 column 01")
                print("\n")
            else:
                print(f"Reserving seat: row {pasnger_row_number} column {pasnger_seat_column}")

# Initializing variables
reserved_f_class = 0
reserved_b_class = 0
reserved_e_class = 0

# Main program loop
while True:
    # Calculate total number of reserved seats
    reserved_f_class = sum(row.count('Reserved') for row in f_class_seats)
    reserved_b_class = sum(row.count('Reserved') for row in b_class_seats)
    reserved_e_class = sum(row.count('Reserved') for row in e_class_seats)

    # Check if all seats are reserved
    if reserved_f_class == F_CLASS_CAP and reserved_b_class == B_CLASS_CAP and reserved_e_class == E_CLASS_CAP:
        print("No more available seats!")
        print("Reservation Type:", passenger_input)
        print("Total number of seats:")
        print("First Class:", F_CLASS_CAP)
        print("Business Class:", B_CLASS_CAP)
        print("Economy Class:", E_CLASS_CAP)

        print("Total number of seats reserved:")

        print("First Class:", reserved_f_class)

        print("Business Class:", reserved_b_class)

        print("Economy Class:", reserved_e_class)
        print("\n")

        passenger_input = input("Enter your letter choice for your class of travel (or 'Q' to quit): ").upper()
        if passenger_input == "Q":
            print("YOU HAVE QUIT THE UCC Signature Express Limited reservation system")
            print("Total number of seats:")
            print("First Class:", F_CLASS_CAP)
            print("Business Class:", B_CLASS_CAP)
            print("Economy Class:", E_CLASS_CAP)
            print("Total number of seats reserved:")
            print("First Class:", reserved_f_class)
            print("Business Class:", reserved_b_class)
            print("Economy Class:", reserved_e_class)
            break
    else:
        print("\n")
        passenger_menu()
        passenger_input = input("Enter your letter choice for your class of travel: ").upper()

        if passenger_input == "F":
            reserve_seat(f_class_seats, "First Class")
        elif passenger_input == "B":
            reserve_seat(b_class_seats, "Business Class")
        elif passenger_input == "E":
            reserve_seat(e_class_seats, "Economy Class")
        elif passenger_input == "Q":
            print("YOU HAVE QUIT THE UCC Signature Express Limited reservation system")
            print("Total number of seats:")
            print("First Class:", F_CLASS_CAP)
            print("Business Class:", B_CLASS_CAP)
            print("Economy Class:", E_CLASS_CAP)
            print("Total number of seats reserved:")
            print("First Class:", reserved_f_class)
            print("Business Class:", reserved_b_class)
            print("Economy Class:", reserved_e_class)
            break
        else:
            print("Invalid option!")