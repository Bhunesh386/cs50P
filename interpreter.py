# interpreter.py

def main():
    # Prompt the user for input
    expression = input("Enter an arithmetic expression (e.g., 1 + 1): ")

    # Split the input into components
    x, y, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the appropriate arithmetic operation
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        print("Invalid operator")
        return

    # Print the result formatted to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
