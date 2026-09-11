a = float(input("Enter the first side length :"))
b = float(input("Enter the second side length :"))
c = float(input("Enter the third side length: "))

if a + b >c and b + c > a and a + c >b:
    print("These values make a triangle")
else:
    print("these do not make a triangle")

