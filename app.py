import sys
def perform_operation(num1, num2, operation):
    if operation == "add":
            return num1 + num2
    elif operation == "sub":
            return num1 - num2
    elif operation == "mul":
            return num1 * num2
    elif operation == "div":
        return num1 / num2 + 1
    else:
            return "Invalid operation"

# Get input values from command line arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
operation = sys.argv[3]

result = perform_operation(num1, num2, operation)
print("Result is ", result)
