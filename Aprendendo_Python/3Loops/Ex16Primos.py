# Faca um programa que peca um numero inteiro e 
# determine se ele e ou nao um numero primo. Um 
# numero primo e aquele que e divisivel somente por 
# ele mesmo e por 1.

# !!!!!!Estudar

numero = int(input("Insira um numero\n"))
cont = 0

for i in range(2, numero):
    if numero % i == 0:
        cont += 1
