x = float (input("first number: "))
y = float (input("second number: "))
operation = input("Operation: ")

Result = None

if operation == "+":
    result = x + y
if operation == "-":
    result = x - y
if operation == "*":
    result = x*y
if operation == "/":
    result = x/y
else :
    print("Unsupported operation")
if result is not None:
    print("Result: ", result)



