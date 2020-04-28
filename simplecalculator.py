# Simple calculator

def add(x, y):
    return x + y

# subtract function

def subtract(x, y):
    return x - y

# Multiplication function

def multiply(x, y):
    return x * y

# divison function

def divide(x, y):
    return x / y   
print(" Select Operations")
print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Divide")

# take a choice from the user

choice = input("\nEnter Choice(1 / 2 /3 / 4)\n")

num1 = float(input("\nEnter first number\n"))
num2 = float(input("\nEnter second number\n"))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("\nInvalid input\n")  