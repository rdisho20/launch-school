# First Car, Adding the Year
car = {
    'type': 'sedan',
    'color': 'blue',
    'mileage': 80_000,
}

car['year'] = 2003

# 3 - Broken Odometer
del car['mileage']

# 4 - What Color?
print(car['color'])

# 5 - What's My length?
print(len(car))

# 6 - Check Key Existence
student = {
    'id': 123,
    'grade': 'B',
}

print(student.get('name'))
print(student.get('grade'))

# w/ membership operator
print('name' in student)    # False
print('grade' in student)   # True

# 7 - Multiple Cars
{
    'car': {
        'type': 'sedan',
        'color': 'blue',
        'year': 2003,
    },
    'truck': {
        'type': 'pickup',
        'color': 'red',
        'year': 1998,
    },
}

# 8 - Which collection?
car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003],
]

# 9 - Divided by Two
numbers = {
    'high':     100,
    'medium':   50,
    'low':      25,
}

half_numbers = []
for item in numbers:
    number = numbers[item]
    half_numbers.append(number // 2) # integer division

print(half_numbers)

# w/ list comprehension and dict.values()
half_numbers = [(value // 2) for value in numbers.values()]  
print(half_numbers)

# 10 - Labeled Numbers
numbers = {
    'high':     100,
    'medium':   50,
    'low':      10,
}
# returns list w/ tuples
# print(numbers.items())

for number in numbers.items():
    print(f"A {number[0]} number is {number[1]}.")

# LS solution:
for key, value in numbers.items():
    print(f"A {key} number is {value}.")