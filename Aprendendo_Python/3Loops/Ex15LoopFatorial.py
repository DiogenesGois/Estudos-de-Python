# programa de calculo do fatorial, permitindo ao 
# usuario calcular o fatorial varias vezes e limitando
# o fatorial a numeros inteiros positivos e menores 
# que 16.

fatorial = int(input("Insira o numero\n"))

while fatorial != 0:
    if fatorial > 0 and fatorial < 16:
        x = 1
        for i in range(1, fatorial + 1):
            x *= i
        
        print(x)

        fatorial = int(input("Insira o numero\n"))
    else:
        print("Valor invalido")