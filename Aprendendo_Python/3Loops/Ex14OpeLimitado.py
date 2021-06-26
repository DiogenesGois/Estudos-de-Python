# Faca um programa que, dado um conjunto de numeros 
# de 0 a 1000, determine o menor valor, o maior valor 
# e a soma dos valores.

maior = 0
menor = 100000
soma = 0

numero = int(input("Insira um numero\n"))  
if numero > 0 and numero < 1000:
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
else:
    print("Valor invalido")   

    





