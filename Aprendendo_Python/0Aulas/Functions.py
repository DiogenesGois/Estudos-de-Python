############# Functions #############

def say_hi():
    print("Hello, User")

def Name(name):
    print("Hello, " + name)

def Age(name, age):
    print("Hello, " + name + ", you are " + age)

print("Top")

word = input("Tell us you name\n")
num = input("And your age\n")

say_hi()

Name(word)

Age(word, num)

print("Bottom")

############# Function - Return Statement #############

def Cube(number):
    return number * number * number

result = Cube(4)
print(result)