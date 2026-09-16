number = 5
factorial = 1
current = number

while current > 1:
    factorial *= current
    current -= 1

print(f"{number}! = {factorial}")
