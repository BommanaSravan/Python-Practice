# # 1. Write a Python program to convert kilometers to miles?

# # 1 mile=1.609 Kms

# m=int(input('Enter the distace in Kms'))

# print(m/1.609)


# # 2.Write a Python program to convert Celsius to Fahrenheit?


# c=int(input('Enter the distace in celsius'))

# print((c*(9/5))+32)

# # # 3. Write a Python program to display calendar?

# import calendar

# print(calendar.month(2023, 12))

# print(calendar.calendar(2023))

# # 4. Write a Python program to solve quadratic equation?

import math

print("ax^2 + bx^1 + c = 0")
print("Enter the coeff a, b and constant c")

a = int(input(("Enter the coeff a: ")))
b = int(input(("Enter the coeff b: ")))
c = int(input(("Enter the constant c: ")))

d = (b**2) - (4*a*c)

root1 = ((-1*b)+(math.sqrt(d))) / (2*a)
root2 = ((-1*b)-(math.sqrt(d))) / (2*a)

print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The solutions are: {} and {}'.format(root1, root2))


# # 5. Write a Python program to swap two variables without temp variable?

a=20
b=30

b=b+a
a=b-a
b=b-a
print(a,b)
