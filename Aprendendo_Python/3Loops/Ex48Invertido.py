# Inverter numero

numero = int(input("Insira um numero\n"))# 123
reverse = 0
resto = 0

while numero != 0: 
    reverse *= 10 # 320
    resto = numero % 10 # 1
    reverse += resto # 321
    numero = int(numero / 10) # 0

print(reverse)