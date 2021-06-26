# par impar

par = 0
impar = 0

for i in range(11):
    numero = int(input("Insira um numero\n"))

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("Pares:", par)
print("Impares:", impar)
