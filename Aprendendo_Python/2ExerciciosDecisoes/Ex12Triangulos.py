# triangulos

lado1 = float(input("Insira o tamanho do lado 1\n"))
lado2 = float(input("Insira o tamanho do lado 2\n"))
lado3 = float(input("Insira o tamanho do lado 3\n"))



if (lado1 + lado2) > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("Triangulo Equilatero")
    elif lado1 == lado2 and lado1 != lado3:
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")
else:
    print("Os valores nao formam um triangulo")


