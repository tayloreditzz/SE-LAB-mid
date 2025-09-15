import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4*a*c

if d < 0:
    print("No real roots")
elif d == 0:
    x = -b / (2*a)
    print("One root:", x)
else:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two roots:", x1, "and", x2)