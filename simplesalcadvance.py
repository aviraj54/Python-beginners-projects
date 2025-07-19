def calculate(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2 == 0:
            return "Error: Division by zero!"
        return n1 / n2
    elif op == '^':
        return n1 ** n2
    else:
        return "Error: Unknown operator!"

def main():
    print("Welcome to CLI Calculator!")
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Operator (+, -, *, /, ^): ")
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        result = calculate(num1, num2, op)
        print(f"{num1} {op} {num2} = {result}")
        
        if input("Continue? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()
