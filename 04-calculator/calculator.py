number1 = float(input("Enter the first number: "))
operator = input("Enter +, -, *, or /: ")
number2 = float(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
    print("Answer:", result)

elif operator == "-":
    result = number1 - number2
    print("Answer:", result)

elif operator == "*":
    result = number1 * number2
    print("Answer:", result)

elif operator == "/":
    result = number1 / number2
    print("Answer:", result)

else:
    print("Invalid operator")
  
