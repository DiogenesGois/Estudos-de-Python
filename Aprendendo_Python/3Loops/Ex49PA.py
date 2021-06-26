# Progressao aritmetica n termo da serie

# a1 = x
# a2 = x + r

# A3 = a1 + (n - 1) * r

primeiro = int(input("Indique o primeiro termo\n"))
razao = int(input("Indique a razao\n"))
serie = int(input("Indique a serie\n"))
m = 0
soma = 0

for n in range(primeiro, primeiro + serie * razao, razao):
    m = m + 2
    print(n, end = "/")
    print(m - 1, end = " ")

    soma += n + (m - 1)

print("\n", soma)
    

