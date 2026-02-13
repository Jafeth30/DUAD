def show_menu(current_number):
    print("\n=== Calculator ===")
    print("Current number:", current_number)
    print("Choose an option:")
    print(" 1. Addition")
    print(" 2. Subtraction")
    print(" 3. Multiplication")
    print(" 4. Division")
    print(" 5. Clear result")
    print(" 6. Exit")

def read_option():
    text = input("Option (1-6): ").strip()
    try:
        op = int(text)
        if op < 1 or op > 6:
            raise ValueError
        return op
    except ValueError:
        raise ValueError(f"Invalid option: '{text}'. Must be an integer between 1 and 6.")

def read_number(prompt="Enter a number: "):
    text = input(prompt).strip().replace(",", ".")
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"Invalid number: '{text}'. Please enter a valid number (10, 3.5, -2, etc.).")

def add(current, n):
    return current + n

def subtract(current, n):
    return current - n

def multiply(current, n):
    return current * n

def divide(current, n):
    if n == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return current / n

def clear():
    return 0.0

def main():
    current_number = 0.0  # mutable state of the program
    print("Welcome. The initial number is 0.")
    while True:
        show_menu(current_number)
        try:
            option = read_option()

            if option == 6:
                print("Exiting... Thank you for using the calculator!")
                break

            if option == 5:
                current_number = clear()
                print("Result cleared. Current number = 0.")
                continue

            # For options 1-4 we need a number
            n = read_number("Enter the number to operate with: ")

            if option == 1:
                current_number = add(current_number, n)
            elif option == 2:
                current_number = subtract(current_number, n)
            elif option == 3:
                current_number = multiply(current_number, n)
            elif option == 4:
                current_number = divide(current_number, n)

            print("New current number:", current_number)

        except ZeroDivisionError as zde:
            print("Error:", zde)
        except ValueError as ve:
            print("Invalid input:", ve)
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
           
