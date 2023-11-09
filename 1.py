import time

print("Program to swap values of 2 variables!\n")
time.sleep(2)

a = None
b = None

while a is None and b is None:
	try:
		a = input("Value of a: ")
		b = input("Value of b: \n")
	except ValueError:
		input("Invalid Input!")

if input("Do you want to swap the values?(y/n): \n") == "y":
	c = a
	a = b
	b = c
else: 
	None

print(f"Value of A = {a} and Value of B = {b}")
