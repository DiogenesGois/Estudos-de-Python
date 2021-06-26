# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salario: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input("Insira o nome\n")
idade = int(input("Insira a idade\n"))
salario = int(input("Insira o salario\n"))
sexo = input("Insira o sexo\n")
estado_civil = input("Insira o estado civil\n") 

while len(nome) < 4:
    nome = input("Insira o nome\n")

while idade < 0 or idade > 150:
    idade = int(input("Insira a idade\n"))

while salario <= 0:
    salario = int(input("Insira o salario\n"))

while sexo != 'm' and sexo != 'f':
    sexo = input("Insira o sexo\n")

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
    estado_civil = input("Insira o estado civil\n") 