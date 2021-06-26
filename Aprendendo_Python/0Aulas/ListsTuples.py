############# Lists/Vetor #############

lucky_numbers = [4, 8, 15, 42, 23, 6]
friends = ['Kevin', 'Karen', 'Jim','Jim','Oscar', 'Toby']

friends[1] = "Mike"

print(friends[-1])
print(friends[1:])
print(friends[1:3])
print(friends)

friends.extend(lucky_numbers)
friends.append('Creed')
friends.insert(1, "Kelly")
friends.remove("Jim")
# friends.clear()
friends.pop()
print(friends)
print(friends.index("Kevin"))
print(friends.count("Jim"))
# friends.sort()
friends.reverse()
print(friends)
friends2 = friends.copy()
print(friends2)
# lucky_numbers.sort()
print(lucky_numbers)

################## Tuples #####################
# Usada em valores fixos
coordinates = [(4, 5), (56, 23), (56, 8, 41)]
# coordinates[1] = 10 error
print(coordinates[0])


