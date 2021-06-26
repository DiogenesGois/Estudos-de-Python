# treino fatorial
from math import factorial

# print(factorial(5))
# print(pow(2,3))

fatorial = int(input("Insira o numero\n"))# 5
x = 1


for i in range(1, fatorial + 1):
    x *= i


print(x)