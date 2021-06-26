# Nota do aluno

nota1 = float(input("Insira a primeira nota\n"))
nota2 = float(input("Insira a segunda nota\n"))
media = (nota1 + nota2)/2

if media > 7 and media < 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distincao")
else:
    print("Valor invalido, insira notas de 0 a 10")