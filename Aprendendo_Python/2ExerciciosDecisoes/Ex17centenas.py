# Programa que leia um numero inteiro menor que 1000 e imprima a quantidade de 
# centenas, dezenas e unidades do mesmo. 326 = 3 centenas, 2 dezenas e 6 unidades

numero = int(input("Insira um numero menor que 1000\n")) # 326
centenas = 0
dezenas = 0
unidade = 0


if numero < 1000:
    if numero >= 100:
        centenas = int(numero / 100)
        numero = numero % 100
        dezenas = int(numero / 10)
        unidade = numero % 10 
        print(centenas, "centenas,", dezenas, "dezenas", "e", numero, "unidades")
    else:
        numero = numero % 100 
        dezenas = int(numero / 10) 
        unidade = numero % 10 
        print(dezenas, "dezenas", "e", unidade, "unidades")
else:
    print("Numero fora do intervalo indicado")

