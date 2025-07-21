# Basic Exception Handling Example

try:
    # Ask user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Try to divide the numbers
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: You can't divide by zero!")

except ValueError:
    print("Error: Please enter valid integers!")

finally:
    print("This block always executes (cleanup, closing files, etc.)")
