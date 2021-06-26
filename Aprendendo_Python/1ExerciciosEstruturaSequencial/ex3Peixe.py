# excesso pescaria

peso_limite = 50

peso = float(input("Insira o peso da pescaria\n"))

if peso > 50:
    excesso = peso_limite - peso
    excesso *= -1
    multa = excesso * 4
    print("Excedeu: ", excesso, "Kg")
    print("Tem ", multa,"Rs de multa a pagar")
else:
    print("Nao excedeu o peso limite, nao tem multa a pagar")




