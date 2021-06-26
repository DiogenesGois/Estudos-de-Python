# Produto mais barato

produ1 = float(input("Insira o valor do primeiro produto\n"))
produ2 = float(input("Insira o valor do segundo produto\n"))
produ3 = float(input("Insira o valor do terceiro produto\n"))

if produ1 < produ2 and produ1 < produ3:
    print("Deve comprar o primeiro produto")
elif produ2 < produ1 and produ2 < produ3:
    print("Deve comprar o segundo produto")
else:
    print("Deve comprar o terceiro produto")