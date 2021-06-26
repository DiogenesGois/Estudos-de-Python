# calcula o peso ideal homem/mulher

altura = float(input("Indique sua altura\n"))

genero = input("Indique o seu genero\n")

if genero == "homem":
    peso_ideal_homen = (72.7*altura) - 58
    print("O seu peso ideal e: ", peso_ideal_homen, "Kg")
elif genero == "mulher":
    peso_ideal_mulher = (62.1*altura) - 44.7
    print("O seu peso ideal e: ", peso_ideal_mulher, "Kg")

