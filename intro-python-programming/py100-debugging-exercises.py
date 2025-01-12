# 1 - Reading Error messages
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

"""Answer:
TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
As the typeerror mentions, 6 positional arguments were given when the function only accepts 1

TypeError: 'int' object is not iterable
As the typeerror mentions, an integer is not an iterable... it is an immutable object
"""

# 2 - Weather Forecast
import random

def predict_weather():
    sunshine = random.choice([True, False]) # <----

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()

"""Why same initially?
...boolean values strings initially
"""

# 3 - Multiply by Five
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(int(number))}!") # <----

"""Answer:
anything input is always taken as a 'string',
thus it needs to be converted to 'int'
"""

# 4 - Pets
pets = { 
    'cat': 'pepe',
    'dog': ['sparky', 'fido'],
    'fish': 'oscar'
}

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# 5 - Confucius Says
def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

"""Answer:
The problem is... none of the conditions return any data
...to fix, add 'return' keyword in front of each string inside the 'if's
"""

# 6 - Populate List
numbers = []

for i in range(1, 6): # <---- change arguements for 'range()'
    numbers.append(i)

print(numbers)

# 7 - Dictionary Access
info = {'name': 'Srdjan', 'age': 38}

print(info.get('nothing', '"Unknown"'))

# 8 - Matrix
import copy

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(copy.copy(sub_list))
    # 
    """
    deepcopy unnecessary because elements of nested are immutable
    ...could also just use 'list.copy()' which creates a shallow copy
    """

matrix[0][0] = "X"
print(matrix)

# LS loop used:
for _ in range(3):
    matrix.append(sub_list.copy())

# 9 - Find Maximum
def find_maximum(numbers):
    if not numbers:
        return None
    # originally wanted to do -inf but this came to mind
    max_number = min(numbers)
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

# 10 - Digit Product
def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0
