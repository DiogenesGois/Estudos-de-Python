# anos bissextos

ano = int(input("Insira um ano: \n"))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 and ano % 100 != 0):
    print("O ano indicado e bissexto")
else:
    print("O ano indicado nao e bissexto")