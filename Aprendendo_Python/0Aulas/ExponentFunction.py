############# Exponent Fuction #############

def raise_to_power(base_num, pow_num):
    result = 1
    for i in range(pow_num):
        result *= base_num
    return result

base = int(input("Insert the base\n"))
powe = int(input("Insert the power\n"))


print(raise_to_power(base, powe))

