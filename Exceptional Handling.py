# 1. Handling Invalid User Input
try:
    number = int(input("Enter an integer: "))
    print("You entered:", number)

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")


# 2. Handling Division by Zero
try:
    numerator = int(input("\nEnter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")


# 3. Handling File Not Found
try:
    file = open("data.txt", "r")
    content = file.read()

    print("\nFile Content:")
    print(content)

    file.close()

except FileNotFoundError:
    print("Error: The file 'data.txt' was not found.")