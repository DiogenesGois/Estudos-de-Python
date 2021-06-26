# Salario e descontos

salario_hora = float(input("Indique o seu salario por hora\n"))
horas_trabalho = float(input("Quantas horas trabalhou?\n"))

salario_bruto = salario_hora * horas_trabalho

IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
Sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (IR + INSS + Sindicato)

print("Salario bruto: ", salario_bruto)
print("IR: ", IR)
print("INSS: ", INSS)
print("Salario liquido: ", salario_liquido)
