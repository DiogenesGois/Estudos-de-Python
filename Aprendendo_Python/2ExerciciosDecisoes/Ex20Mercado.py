# O Hipermercado Tabajara ###INACABADO###

File = True
Alcatra = True
Picanha = True


Tipo = float(input("Indique o tipode carne\n"))
Forma = input("Indique a forma de pagamento\n")
Quantidade = int(input("Indique a quantidade\n"))

if File and Quantidade <= 5 and Forma == "cartao":
    preco = Quantidade * 4.90
    print()