seconds = int(input("Enter seconds: "))

hours = seconds // 3600
remaining = seconds % 3600

minutes = remaining // 60
seconds_left = remaining % 60

print(hours, "hours", minutes, "minutes", seconds_left, "seconds")