# Sequencia de fibonacci

# n = int(input("Que termo deseja encontrar: "))
# ultimo = 1
# penultimo = 1

# if (n == 1) or (n == 2):
#     print("1")
# else:
#     for i in range(2,n):
#         termo = ultimo + penultimo # 3
#         penultimo = ultimo # 2
#         ultimo = termo # 3
#         i += 1
#     print(termo)
    

ultimo = 1
penultimo = 1

for i in range(501):
    termo = ultimo + penultimo # 3
    penultimo = ultimo # 2
    ultimo = termo # 3

    print(termo)