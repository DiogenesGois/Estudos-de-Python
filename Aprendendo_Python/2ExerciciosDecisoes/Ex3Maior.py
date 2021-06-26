# mostrar numero maior entre os 3

num1 = input("Insira um numero\n")
num2 = input("Insira um numero\n")
num3 = input("Insira um numero\n")

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)