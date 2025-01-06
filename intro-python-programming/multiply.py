def product(first, second):
    return float(first) * float(second)

first_num = input("Enter the first number: ")
second_num = input("Enter the second number: ")

print(f'{first_num} * {second_num} = {product(first_num, second_num)}')