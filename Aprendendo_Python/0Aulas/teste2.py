############# Practice #############       
# Faça um programa que leia um nome de usuário e 
# a sua senha e não aceite a senha igual 
# ao nome do usuário, mostrando uma mensagem
# de erro e voltando a pedir as informações.

nome_usuari = input("Digite o seu nome de usuario?")

senha = input("Digite a sua senha")


while nome_usuari == senha:
    print("Nome e senha invalidos")
    nome_usuari = input("Digite o seu nome de usuario?")
    senha = input("Digite a sua senha")

print("Bem vindo!")