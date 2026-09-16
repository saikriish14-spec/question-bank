
year = int(input("Enter a year: "))

if year % 100 == 0:
    print(f"{year} is a century year.")
   
    if year % 400 == 0:
        print(f"It is also a leap year!")
    else:
        print(f"However, it is NOT a leap year.")
else:
    print(f"{year} is NOT a century year.")
    

