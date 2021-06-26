############# While Loops #############

# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop")

############# Guessing Game #############

# i = 1
# num = 568
# guess = 0

# guess = int(input("Guess the number\n"))

# if guess != num:
#     while guess != num:
#         guess = int(input("Wrong number, try again\n"))


# print("Well done!")

# i = 1
# num = 568
# guess = 0
# out_of_guesses = False
# guess_limit = 3

# guess = int(input("You have 10 attempts to guess the number\n"))


# while guess != num and not(out_of_guesses):
#     if i < guess_limit:
#         guess = int(input("Wrong number, try again\n"))
#         i += 1
#     else:
#         out_of_guesses = True


# if out_of_guesses:
#     print("You ran a out of guesses")
# else:
#     print("Well done!") 

############# Practice #############       

    
nome_usuari = input("Digite o seu nome de usuario:   ")

senha = input("Digite a sua senha:   ")


while nome_usuari == senha:
    print("Nome e senha invalidos")
    nome_usuari = input("Digite o seu nome de usuario:   ")
    senha = input("Digite a sua senha:   ")

print("Bem vindo!")


