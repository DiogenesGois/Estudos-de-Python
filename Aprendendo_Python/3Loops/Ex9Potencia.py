# potencia

base = int(input("Indique a base\n"))
expo = int(input("Indiqueo expoente\n"))
powe = 1

for i in range(expo):
    powe *= base

print(powe)