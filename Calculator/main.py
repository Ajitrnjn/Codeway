# Dictionary mapping operator symbols to their corresponding functions
from operation import operations


def main():
    # Get user input for numbers
    num1 = 0
    num2 = 0
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    op_choice = ''

    # Get user input for operation
    while True:
        op_choice = input("Enter the operator symbol: ")
        if op_choice in operations:
            break
        else:
            print("Invalid operator symbol. Please choose from the available "
                  "operations.")

    # Perform the calculation
    return operations[op_choice](num1, num2)


if __name__ == '__main__':
    # Display the result
    print("Result : ", main())