# # import math
# from math import sqrt, floor
# num = int(input("Insira um numero\n"))
# raiz =   sqrt(num)


# print('A raiz de {} e igual a {:.2f}'.format(num, raiz))

# print(factorial(5))
# print(pow(2,3))

import random

num = random.random()
num = random.randint(1, 10)


print(num)


print("Hello World \U0001F30E")

####### Exercicio #######
# 1 - programa que mostre parte inteira de umnumero real
# from math import trunc

# num = float(input("Indique o numero\n"))

# print("A parte inteira de {:.2f} e {}".format(num, trunc(num)))


# 2 - calcular hipotenusa
from math import hypot

oposto = float(input("Insira o cateto oposto\n"))
adjacente = float(input("Insira o cateto adjacente\n"))

print("A hipotenusa e: {:.2f}".format(hypot(oposto, adjacente)))

