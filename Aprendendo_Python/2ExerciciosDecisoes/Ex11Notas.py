# media de aproveitamento:
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E

nota1 = float(input("Insira a primeira nota\n"))
nota2 = float(input("Insira a segunda nota\n"))

media = (nota1 + nota2) / 2

print("\nNota 1:", nota1,)
print("Nota 2:", nota2,)
print("Media:", media,)


if media < 6:
    print("Nota D")
    print("Reprovado")
elif media < 7:
    print("Nota C")
    print("Aprovado")
elif media < 8:
    print("Nota B")
    print("Aprovado")
elif media < 9:
    print("Nota A")
    print("Aprovado")
else:
    print("Valor invalido")
    


