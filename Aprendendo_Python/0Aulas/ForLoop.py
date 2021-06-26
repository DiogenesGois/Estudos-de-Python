############# For Loops #############

# list_of_friends = ["Jim", "Karen", "Kevin"]
# for each_friend in list_of_friends:
#     print(each_friend)

# for index in range(10):
#     print(index)

# for index2 in range(3, 10):
#     print(index2)

# friends = ["Jim", "Karen", "Kevin"]
# for index3 in range(len(friends)):
#     print(friends[index3])

# for index4 in range(5):
#     if index4 == 0:
#         print("First Iteration")
#     else:
#         print("Not first") 

# for index2 in range(3, 10, 2):
#     print(index2)

############# Practice #############

# numero = [1, 2, 3]

# for i in range(len(numero)):
#     numero[i] = int(input("Insira um numero\n"))

# for j in range(len(numero)):
#     print(j, numero[j])
   
soma = 0
max = 0
min = 100000
numero = [1, 2, 3, 4, 5]

for i in range(len(numero)):
    numero[i] = int(input("Insira um numero\n"))
    soma += numero[i]

    if numero[i] <= min:
        min = numero[i]
    
    if numero[i] >= max:
        max = numero[i]

print(max)
print(min)
print(soma)
print(soma/len(numero))
