# Rajuste de salario

salario = float(input("Insira o salario\n"))
salario2 = salario
aumento1 = salario * 0.2
aumento2 = salario * 0.15
aumento3 = salario * 0.1
aumento4 = salario * 0.05


if salario <= 280:
    salario += aumento1
    print("Salario atual: ", salario2)
    print("Aumento de 20%: ", aumento1)
    print("O seu salario passara a ser", salario)
elif salario > 280 and salario < 700:
    salario += aumento2
    print("Salario atual: ", salario2)
    print("Aumento de 15%: ", aumento2)
    print("O seu salario passara a ser", salario)
elif salario >= 700 and salario < 1500:
    salario += aumento3
    print("Salario atual: ", salario2)
    print("Aumento de 10%: ", aumento3)
    print("O seu salario passara a ser", salario)
else:
    salario += aumento4
    print("Salario atual: ", salario2)
    print("Aumento de 5%: ", aumento4)
    print("O seu salario passara a ser", salario)


