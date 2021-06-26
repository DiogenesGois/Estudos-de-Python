# multibanco

valor = int(input("Indique o valor a levantar\n")) # 266
nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
nota5 = 0

if valor >= 100:
    nota1 = int(valor / 100)
    valor -= nota1 * 100
    print(nota1, "de 100")

if valor >= 50:
    nota2 = int(valor / 50)
    valor -= nota2 * 50
    print(nota2, "de 50")

if valor >= 10:
    nota3 = int(valor / 10)
    valor -= nota3 * 10
    print(nota3, "de 10")

if valor >= 5:
    nota4 = int(valor / 5)
    valor -= nota4 * 5
    print(nota4, "de 5")

if valor >= 1:
    nota5 = int(valor / 1)
    valor -= nota5
    print(nota5, "de 1")








