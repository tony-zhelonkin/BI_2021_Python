# This is my first GitHub project - "The Calculator"

a = int(input("Please input first digit: ", )) # input first digit
oper = input("Please input +,-,* or /: ", ) # input operation
b = int(input("Please input second digit: ", )) # input second digit

if oper == "+":
    print(a + b)
elif oper == "-":
    print(a - b)
elif oper == "*":
    print(a * b)
elif oper == "/":
    print(a / b)
else:
    print("Error! Second input should an operation: +, -, * or /")
