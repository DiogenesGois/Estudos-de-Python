# Loja de tintas


metros_quadrados = int(input("Insira o tamanho em metros quadrados\n"))
litros = metros_quadrados / 3
preco = 80.00
capacidade = 18

latas = litros / capacidade
total = latas * preco

print("Ira precisar de ", latas)
print("\nE custara ", total, "Rs")

   
