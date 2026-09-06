# Welcome to modular packager program

import random
import uuid
import math_utils
import string_utils
import helper
import greet
from utilities import file_utils, date_utils
from shapes import circle as shape_circle, rectangle
from geometry import triangle

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Current Date and Time: {date_utils.get_current()}")
            helper.divider()
        elif choice == '2':
            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")
            print(f"Difference: {date_utils.get_difference(d1, d2)} days")
            helper.divider()
        elif choice == '3':
            fmt = input("Enter format (e.g., %d/%m/%Y): ")
            print(f"Formatted Date: {date_utils.format_custom(fmt)}")
            helper.divider()
        elif choice == '4':
            print(f"Elapsed Time: {date_utils.stopwatch()} seconds")
            helper.divider()
        elif choice == '5':
            sec = int(input("Enter seconds: "))
            date_utils.countdown(sec)
            helper.divider()
        elif choice == '6':
            break

def math_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            n = int(input("Enter a number: "))
            print(f"Factorial: {math_utils.calculate_factorial(n)}")
            helper.divider()
        elif choice == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            print(f"Compound Interest: {math_utils.calculate_compound_interest(p, r, t):.2f}")
            helper.divider()
        elif choice == '3':
            angle = float(input("Enter angle in degrees: "))
            s, c, t = math_utils.calculate_trigonometry(angle)
            print(f"Sin: {s:.4f}, Cos: {c:.4f}, Tan: {t:.4f}")
            helper.divider()
        elif choice == '4':
            print("1. Circle\n2. Rectangle\n3. Triangle")
            shape = input("Choose shape: ")
            if shape == '1':
                r = float(input("Enter radius: "))
                print(f"Area: {shape_circle.area(r):.2f}")
            elif shape == '2':
                l, w = float(input("Length: ")), float(input("Width: "))
                print(f"Area: {rectangle.area(l, w):.2f}")
            elif shape == '3':
                b, h = float(input("Base: ")), float(input("Height: "))
                print(f"Area: {triangle.area(b, h):.2f}")
            helper.divider()
        elif choice == '5':
            break

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            print(f"Random Number: {random.randint(1, 100)}")
            helper.divider()
        elif choice == '2':
            length = int(input("Enter list length: "))
            print(f"Generated List: {[random.randint(1, 100) for _ in range(length)]}")
            helper.divider()
        elif choice == '3':
            length = int(input("Enter password length: "))
            chars = string_utils.generate_random_password_chars()
            print(f"Password: {''.join(random.choice(chars) for _ in range(length))}")
            helper.divider()
        elif choice == '4':
            print(f"Generated OTP: {random.randint(100000, 999999)}")
            helper.divider()
        elif choice == '5':
            break

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file\n2. Write to a file\n3. Read from a file\n4. Append to a file\n5. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice in ['1', '2', '3', '4']:
            filename = input("Enter file name: ")
            if choice == '1': file_utils.create_file(filename)
            elif choice == '2': file_utils.write_file(filename, input("Enter data: "))
            elif choice == '3': file_utils.read_file(filename)
            elif choice == '4': file_utils.append_file(filename, input("Enter data: "))
            helper.divider()
        elif choice == '5':
            break

def main():
    while True:
        greet.show_welcome()
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        helper.divider()
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            datetime_menu()
        elif choice == '2':
            math_menu()
        elif choice == '3':
            random_menu()
        elif choice == '4':
            print(f"\nGenerated UUID: {uuid.uuid4()}")
            helper.divider()
        elif choice == '5':
            file_menu()
        elif choice == '6':
            mod = input("\nEnter module name to explore: ")
            try:
                print(f"Attributes: {dir(__import__(mod))[:20]} ...")
            except ImportError:
                print("Module not found.")
            helper.divider()
        elif choice == '7':
            greet.show_exit()
            break

if __name__ == '__main__':
    main()
