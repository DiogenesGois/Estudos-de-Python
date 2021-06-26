# maior dos 5 numeros

maior = 0

for i in range(5):
    numero = int(input("Insira um numero\n"))    
    if numero > maior:
        maior = numero

print("O maior numero foi: ", maior)