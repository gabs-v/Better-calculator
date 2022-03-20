#Getting to make a calculator that can either add, subtract, multiply, or divide! :)

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op  == "+":
    print(num1+num2)

elif op == "-":
    print(num1 - num2)

elif op == "/":
    print(num1 / num2)

elif op == "*":
    print(num1*num2)

else:
    print("Invaled operator")