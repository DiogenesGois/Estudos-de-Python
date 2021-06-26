# mostrar maior e menor

num1 = input("Insira um numero\n")
num2 = input("Insira um numero\n")
num3 = input("Insira um numero\n")


if num1 > num2 and num1 > num3:
    print(num1)
    if num2 < num3:
        print(num2)
    else:
        print(num3)
elif num2 > num1 and num2 > num3:
    print(num2)
    if num1 < num3:
        print(num1)
    else:
        print(num3)
else:
    print(num3)
    if num1 < num2:
        print(num1)
    else:
        print(num2)
