# Soma e media dos numeros

soma = 0


for i in range(1, 6):
    numero = float(input("Insira um numero\n"))
    soma += numero

media = soma/i

print("Soma:", soma)
print("Media:", media)