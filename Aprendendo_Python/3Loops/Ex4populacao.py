# o numero de anos necessarios para que a populacao do pais 
# A(3%) ultrapasse ou iguale a populacao do pais B(1.5%), mantidas as
#  taxas de crescimento.

# paisA = int(input("Insira a populacao do pais A\n"))
# paisB = int(input("Insira a populacao do pais B\n"))
# taxaA = float(input("Insira a taxa de crescimento do pais A\n"))
# taxaB = float(input("Insira a taxa de crescimento do pais B\n"))

# cont = 0

# while paisA <= paisB:
#     paisA += paisA * (taxaA / 100)
#     paisB += paisB * (taxaB / 100)
#     cont += 1

# print(cont)

popA = int(input("Populacao do pais A: "))
while popA<0:
    popA = int(input("Populacao do pais deve ser maior que 0: "))

taxaA = float(input("Taxa de crescimento da cidade A: "))

popB = int(input("Populacao do pais B: "))
while popB < 0:
    popB = int(input("Populacao do pais deve ser maior que 0: "))

taxaB = float(input("Taxa de crescimento da cidade B: "))

ano=0
while popA < popB:
    ano += 1
    popA = int((1 + (taxaA/100) )* popA)
    popB = int((1 + (taxaB/100) )* popB)
    print("Ano:", ano)
    print("Populacao A: %d" % popA)
    print("Populacao B: %d\n\n" % popB)

print("Ultrapassa no ano:",ano)
