# Ginastica

maior = 0
menor = 100000
media = 0
soma = 0
cont = 0

atleta = input("Indique o atleta\n")

while cont < 7:
    nota = float(input("Insira a nota\n"))

    if nota < menor:
        menor = nota
    
    if nota > maior:
        maior = nota

    soma += nota
    cont += 1

media = (soma - menor - maior) / 5

print("Resultado Final:")
print("Atleta:", atleta)
print("Melhor nota:", maior)
print("Pior nota:", menor)
print("Media:", media)
