## Task - 2 Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mult(x, y):
    return x * y

def divide(x, y):
    if y==0:
        return " Error: Division by zero"
    return x / y

print("select operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice(1/2/3/4):"))

num1 = float(input("Enter First Number here: "))
num2 = float(input("Enter Second Number here: "))

if choice == 1:
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == 2:
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == 3:
    print(f"{num1} * {num2} = {mult(num1, num2)}")
elif choice == 4:
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid Input")