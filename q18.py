


num1 = float(input("Enter a number :"))
num2 = float(input("Enter the second number :"))
op = input("choose an operator (+,-,*,/,)")


if op =="+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op =="*":
    result = num1 * num2
else:
    if op == "/":
        result = num1/num2


print(f"result is {result}")

