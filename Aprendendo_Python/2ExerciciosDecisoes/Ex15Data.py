# validar a data

dia = int(input("Insira o dia\n"))
mes = int(input("Insira o mes\n"))
ano = int(input("Insira o ano\n"))

if (dia > 0 and dia < 32) and (mes > 0 and mes < 13) and ano > 0:   
    if mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 and ano % 100 != 0):
            if dia > 29:
                print("Data invalida")
            else:
                print(dia,"/",mes,"/",ano)            
        else:
            if dia > 28:
                print("Data invalida")
            else:
                print(dia,"/",mes,"/",ano)
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if dia > 30:
            print("Data invalida")
        else:
            print(dia,"/",mes,"/",ano)
    else:
        if dia > 31:
            print("Data invalida")
        else:
            print(dia,"/",mes,"/",ano)
elif dia < 0 or dia > 31:
    print("Data invalida, alterei o dia")
else:
    print("Data invalida, alterei o mes")   
