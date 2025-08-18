# calculator.py — runs in Terminal (not Jupyter)
import math

def get_float(prompt):
    """Safely get a number from the user."""
    while True:
        x = input(prompt).strip()
        try:
            return float(x)
        except ValueError:
            print("Please enter a number (e.g., 12 or 3.5).")

def add():
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    print("Result:", a + b)

def subtract():
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    print("Result:", a - b)

def multiply():
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    print("Result:", a * b)

def divide():
    a = get_float("Enter first number: ")
    b = get_float("Enter second number: ")
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        print("Result:", a / b)

def square_root():
    n = get_float("Enter a number: ")
    if n < 0:
        print("Error: Cannot take the square root of a negative number.")
        return
    print("Result:", math.sqrt(n))

def main():
    while True:
        print("\nSimple Calculator")
        print("1) Add")
        print("2) Subtract")
        print("3) Multiply")
        print("4) Divide")
        print("5) Square Root")
        print("6) Quit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            add()
        elif choice == "2":
            subtract()
        elif choice == "3":
            multiply()
        elif choice == "4":
            divide()
        elif choice == "5":
            square_root()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
