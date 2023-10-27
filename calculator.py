def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    return num1 / num2

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("Select an operation:")
        print("1 for addition")
        print("2 for subtraction")
        print("3 for multiplication")
        print("4 for division")

        select = int(input("Select (1/2/3/4): "))

        if select < 1 or select > 4:
            print("Enter a valid operation (1/2/3/4)")
            continue

        if select == 1:
            result = add(num1, num2)
        elif select == 2:
            result = subtract(num1, num2)
        elif select == 3:
            result = multiply(num1, num2)
            
        elif select == 4:
            result = divide(num1, num2)

        print(f"Result: {result}")

        next_calculation = input("Enter 'y' for the next calculation or press any other key to exit: ")
        if next_calculation.lower() != 'y':
            print("Thank you")
            break

    except ValueError:
        print("Invalid input. Please enter valid numbers and operation.")
