
print("Calculator:")

num1 = float(input("Insert first number\n")) 

opera = input("Insert the oparator\n") 

num2 = float(input("insert second number\n"))

if opera == "+":
    result = num1 + num2
    print(num1, " + ", num2, " = ", result)

elif opera == "-":
   result = num1 - num2
   print(num1, " + ", num2, " = ", result)

elif opera == "*":
   result = num1 * num2
   print(num1, " + ", num2, " = ", result)

elif opera == "/":
   result = num1 / num2
   print(num1, " + ", num2, " = ", result)

else:
   print("Invalid operator")



