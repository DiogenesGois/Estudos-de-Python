# programa que leia um nome de usuario e a sua senha 
# e nao aceite a senha igual ao nome do usuario

nome = input("Insira o username\n")
passwd = input("Insira a password\n")

while passwd == nome:
    nome = input("Insira o username valido\n")
    passwd = input("Insira a password valida\n")

print("Bem-vindo")
    