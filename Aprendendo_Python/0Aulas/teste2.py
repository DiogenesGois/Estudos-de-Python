############# Practice #############       
# Fa�a um programa que leia um nome de usu�rio e 
# a sua senha e n�o aceite a senha igual 
# ao nome do usu�rio, mostrando uma mensagem
# de erro e voltando a pedir as informa��es.

nome_usuari = input("Digite o seu nome de usuario?")

senha = input("Digite a sua senha")


while nome_usuari == senha:
    print("Nome e senha invalidos")
    nome_usuari = input("Digite o seu nome de usuario?")
    senha = input("Digite a sua senha")

print("Bem vindo!")