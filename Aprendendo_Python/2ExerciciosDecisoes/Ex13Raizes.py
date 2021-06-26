
# from math import*

a = float(input("Insira o valor de A\n"))

if a == 0:
    print("Nao e uma equacao de segundo grau")

b = float(input("Insira o valor de B\n"))
c = float(input("Insira o valor de C\n"))

delta = (b ** 2) - 4 * a * c

raiz1 = ((-b) + (delta ** (1/2))) / 2 * a
raiz2 = ((-b) - (delta ** (1/2))) / 2 * a


if delta < 0:
    print("A equacao nao possui raizes reais")
elif delta == 0:
    print("Tem apenas uma raiz: ", raiz2)
else:
    print("Raiz 1: ", raiz1)
    print("Raiz 2: ", raiz2)
    
