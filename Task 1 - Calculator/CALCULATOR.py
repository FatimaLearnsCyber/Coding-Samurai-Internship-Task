while True:
    print("\nSUPPORTED OPERATIONS: +, -, *, /, %, **, //")
    print("Enter 'exit' as the operator to quit the calculation.")

    try:
        num1 = int(input("ENTER THE FIRST NUMBER: "))
    except ValueError:
        print("Kindly enter a valid number!")
        continue
    operator = (input("ENTER THE OPERATOR: "))
    if operator.lower() == "exit":
        print("Exiting the calculator!")
        break
    try:
        num2 = int(input("ENTER THE SECOND NUMBER: "))
    except ValueError:
        print("Kindly enter a valid number!")
        continue
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        if num2 == 0:
            print("ERROR: Division by ZERO is not allowed")
        else:
            print(num1 / num2)
    elif operator == "%":
        print(num1 % num2)
    elif operator == "**":
        print(num1 ** num2)
    elif operator == "//":
        print(num1 // num2)
    else:
        print("INVALID OPERATOR. PLEASE USE ONE OF +, -, *, /, %, **, //, or 'exit'.")