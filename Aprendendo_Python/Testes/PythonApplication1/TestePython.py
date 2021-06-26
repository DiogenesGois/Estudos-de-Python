salario_hora = float(input("Indique o seu salario por hora\n"))
horas_trabalho = float(input("Quantas horas trabalhou?\n"))

salario_bruto = salario_hora * horas_trabalho
salario_liquido = 0

INSS = salario_bruto * 0.1
Sindicato = salario_bruto * 0.03
FGTS = salario_bruto * 0.11

print("Salario bruto: ", salario_bruto)

if salario_bruto <= 900:
    salario_liquido = salario_bruto    
    print("Isento de descontos")
    print("Salario liquido: ", salario_liquido) 
elif salario_bruto >= 900 and salario_bruto < 1500:
    IR = salario_bruto * 0.05    
    print("IR (5%): ", IR)
    print("INSS (10%): ", INSS)
    print("FGTS (11%): ", FGTS)
    print("Total de descontos: ", IR + INSS + Sindicato + FGTS)
    salario_liquido = salario_bruto - (IR + INSS + Sindicato + FGTS)
    print("Salario liquido: ", salario_liquido)
elif salario_bruto >= 1500 and salario_bruto < 2500:
    IR = salario_bruto * 0.1
    print("IR (10%): ", IR)
    print("INSS (10%): ", INSS)
    print("FGTS (11%): ", FGTS)
    print("Total de descontos: ", IR + INSS + Sindicato + FGTS)
    salario_liquido = salario_bruto - (IR + INSS + Sindicato + FGTS)
    print("Salario liquido: ", salario_liquido)
elif salario_bruto >= 2500:
    IR = salario_bruto * 0.2
    print("IR (10%): ", IR)
    print("INSS (10%): ", INSS)
    print("FGTS (11%): ", FGTS)
    print("Total de descontos: ", IR + INSS + Sindicato + FGTS)
    salario_liquido = salario_bruto - (IR + INSS + Sindicato + FGTS)
    print("Salario liquido: ", salario_liquido)
else:
    print("Valor invalido")

