# 1 - First Element
def first(list):
    if list:
        return list[0]
    else:
        return None # empty lists are 'falsy'

print(first(['Earth', 'Moon', 'Mars']))
print(first([]))

# 2 - Last Element
def last(list):
    if list:
        return list[len(list)-1] # or return list[-1] because python supports negative indexing
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))
print(last([]))

# 3 - Add + Delete
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')
print(energy)

# 4 - Alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabetagamma = list(alphabet)

print(alphabetagamma)

# 5 - Filter
scores = [96, 47, 113, 89, 100, 102]
count = 0

for score in scores:
    if score >= 100:
        count += 1

print(count)

""" more pythonic:
scores = [96, 47, 113, 89, 100, 102]

count = sum(1 for score in scores if score >= 100) # 1 is the incrementer

print(count)
"""

# 6 - Vocabulary
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for set in vocabulary:
    for word in set:
        print(word)

# w/ comprehension - all_words = [word for sublist in vocabulary for word in sublist]

# 7 - Equality
list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(id(list1[0]))  # Memory address of element 2
print(id(list1[1]))  # Memory address of element 6
print(id(list1[2]))  # Memory address of element 4
print(id(list2[0]))  # Memory address of element 2
print(id(list2[1]))  # Memory address of element 6
print(id(list2[2]))  # Memory address of element 4

# 8 - Type
some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

def type_check(object):
    if type(object).__name__ == 'list':
        print(f"object holds a list")
    else:
        print(f"object doesn't hold a list")

type_check(some_value1)
type_check(some_value2)

# 9 - Travel
destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city_to_check, itinerary):
    if itinerary.count(city_to_check) > 0:
        return True
    else:
        return False

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

# 10 - Passcode
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
pass_str = '-'.join(passcode)

print(pass_str)

# 11 - Checking items off the grocery list
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

for i in range(len(grocery_list), 0, -1): 
    print(grocery_list.pop())
print(grocery_list)

"""
looping back updates/re-reads current
length :: grocery list updating the range
OR
for _ in range(len(grocery_list)):
    print(grocery_list.pop())
"""