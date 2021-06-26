# imprimir numeros impares
# receber limites
# Soma de todos os numero entre x e y

for i in range(1, 51):
    print(i)


num1 = int(input("Insira o limite inferior\n"))
num2 = int(input("Insira o limite superior\n"))
soma = 0

for i in range(num1, num2 + 1):
    soma += i
    
    
print(soma)