# User Input: Exercises

a = 3
b = 9
c = -3
d = 3.0
e = -9

# Q1

# first_number = (int)input("Enter the first number:")
# second_number = (int)input("Enter the second number:")
# answer = int(first_number) + int(second_number)
#   print(f"{first_number} + {second_number} = {answer}")

print(a + b)
print(c + b)
print(d + e)

print()
# #Q2

# first_number = input("Enter the first number:")
# second_number = input("Enter the second number:")
# answer = first_number * second_number
#   print(f"{first_number} * {second_number} = {answer}")

print(a * b)
print(c * b)
print(d * e)

print()

#Q3 does not yet incorporate the float number?

#kilometers = input("Enter the number of kilometers to convert:")
# answer = kilometers
# print (f"kilometers" * 1000 = {answer} meters")
# print (f"kilometers" * 100000 = {answer} centimeters")

km = int(input("Enter the number of kilometers to convert: "))
m = km * 1000
cm = km * 10000
print(f"Your kilometer value converts to {m} meters or {cm} centimeters.")

print()

#Q4

name = input("Enter your name:")
height = input("Enter your height in centimeters: ")
print(f"Hi, {name} you are {height} cms tall.")
