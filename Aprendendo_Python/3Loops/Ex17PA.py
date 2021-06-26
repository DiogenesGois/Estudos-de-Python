# Progressao aritmetica

termo = int(input("Indique o primeiro termo\n"))
razao = int(input("Indique a razao\n"))
n = termo + 10 * razao


for i in range(termo, n, razao):
    print(i, end = " --> ")

print("ACABOU")
