import pprint

# foist
my_list = [6, 3, 0, 11, 20, 4, 17]
counter = 0

while counter < len(my_list):
    print(my_list[counter])
    counter += 1
print()
for number in my_list:
    print(number)

# print evens w/ while, odds w/ for
my_list = [6, 3, 0, 11, 20, 4, 17]
index = 0

print('Evens:')
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

print('\nOdds:')
for number in my_list:
    if number % 2 != 0:
        print(number)

# Print all even numbers w/o using while loops
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for i in range(len(my_list)):
    for number in my_list[i]:
        if number % 2 == 0:
            print(number)

# another variation
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0
]

new_list = []
for number in my_list:
    if number % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

pprint.pprint(new_list)

# 7 - find_integers function
my_tuple = (1, 'a', '1', 3, [7], 3.1415, -4, None, {1, 2, 3}, False)

def find_integers(lst_obj):
    int_list = []
    for element in lst_obj:
        if type(element) is int:
            int_list.append(element)
    return int_list

integers = find_integers(my_tuple)
pprint.pprint(integers)

# 8 - comprehension -> dict
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = { name: len(name)
            for name in my_set
            if len(name) % 2 != 0 }

pprint.pprint(my_dict)

# 9 - Math doesnt scare me!!!!
def factorial(number):
    result = 1
    for n in range(1, number + 1):
        result *= n
    return result

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

# 10 - randrange!
import random

number = 0
highest = 10

while number != highest:
    number = random.randrange(highest + 1)
    print(number)

# LS solution
highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# 11 - Challenge Problem
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

counter = 0
while counter < len(my_list):
    sub_counter = 0
    while sub_counter < len(my_list[counter]):
        if my_list[counter][sub_counter] % 2 == 0:
            print(my_list[counter][sub_counter])
        sub_counter += 1
    counter += 1


orig = [[1, 2], 3, 4]
dup = orig

print(orig is dup)           # False
print(orig == dup)           # True
orig[2] = 44
print(dup)                   # [[1, 2], 3, 4]

print(orig[0] is dup[0])     # True
orig[0][1] = 22
print(dup[0])                # [1, 22]