
tamanho_arquivo = float(input("Indique o tamanho do arquivo\n"))
velocidade_internet = float(input("Indique a velocidade da internet\n"))

contador = 0

while tamanho_arquivo >= velocidade_internet:
    tamanho_arquivo -= velocidade_internet
    contador += 1

print("o arquivo levara mais ou menos ", contador, " min a baixar")
