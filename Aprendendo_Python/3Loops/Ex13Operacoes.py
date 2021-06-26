# Faca um programa que, dado um conjunto de N numeros, 
# determine o menor valor, o maior valor e a soma dos
# valores.

maior = 0
menor = 100000
soma = 0

numero = int(input("Insira um numero\n"))  

while numero != 0:
    numero = int(input("Insira um numero\n"))

    if numero > maior:
        maior = numero
    
    if numero < menor and numero != 0:
        menor = numero

    soma += numero

print("Maior: ", maior)
print("Menor: ", menor)
print("Soma: ", soma)


