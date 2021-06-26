############# If Statement comparison #############

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3


num1 = input("Write the first number\n")
num2 = input("Write the second number\n")
num3 = input("Write the third number\n")

print(max_num(num1, num2, num3))
