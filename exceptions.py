import sys

#exceptions are useful if you expect errors

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Must be a number")
    sys.exit(1)

try:
    result = x / y
#if this exception happens, print error message
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)


print(f"{x} / {y} = {result}")