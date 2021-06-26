# Programa pede nota ate ser valida


nota = float(input("Insira uma nota\n"))

while nota < 0 or nota > 10:
    nota = float(input("Insira uma nota\n"))

print("A nota inserida:", nota)

