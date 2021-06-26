# inteiro ou decimal? 

numero = float(input('Numero original: '))
print("Arredondado    :", round(numero))


if numero == round(numero):
    print("Inteiro")
else:
    print("Decimal")
    print("Arredondado pra baixo: ", round(numero-0.5) )
    print("Arredondado pra cima : ", round(numero+0.5) )
