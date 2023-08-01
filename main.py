# Building a basic mathematics calculator with Python. Let's start
print("Mathematics Calculator")
first = int(input("Enter your First number: "))
second = int(input("Enter your Second number: "))
user_operation = input("Which operation you want to perform + - * /: ")
if user_operation == "+":
    print(first + second)
elif user_operation == "-":
    print(first - second)
elif user_operation == "*":
    print(first * second)
elif user_operation == "/":
    print(first / second)
else:
    print("Error, Operation is not successful")