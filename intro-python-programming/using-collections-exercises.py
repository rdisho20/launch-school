# 1 - seventh number
print(range(0, 25, 3)[6])

# 2 - slicing
string = 'Launch School'
# print(string[4:10])
sub_string = string[string.find('c'):(string.find('c') + 6)]
print(sub_string)

# 3 - New Toop
toop = (1, 2, 3, 4, 5)
r_listed = list(toop)
r_listed.reverse()
r_listed.pop(len(r_listed)-1)
r_listed.pop(0)
r_toop = tuple(r_listed)

print(r_toop)

"""
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)

OR

toop = (1, 2, 3, 4, 5)
r_toop = tuple(list(toop)[::-1][1:-1])

print(r_toop)
"""

# 4 - 3-parter
pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog']) # 1
print(pets.get('Lizard')) #2
print(pets.get('Lizard', '<silence>')) # 3

# 6 - print?
print('abc-def'.isalpha()) # False
print('abc_def'.isalpha()) # False
print('abc def'.isalpha()) # False
print('abc def'.isalpha() and
      'abc def'.isspace()) # False
print('abc def'.isalpha() or
      'abc def'.isspace()) # False
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) # True
print('-31415'.isdigit()) # False
print('31_415'.isdigit()) # False
print('3.1415'.isdigit()) # False
print(''.isspace()) # False

# 7 - replace
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_split = info.split(':')
info_joined = '+'.join(info_split)
print(info_joined)

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info_replaced = info.replace(':', '+')
print(info_replaced)

"""
info_list = list(info)
for i in range(len(info_list)):
    if info_list[i] == ':':
        info_list[i] = '+'
info = ''.join(info_list)

print(info)
"""

# 8 - Explain
"""
line 3 is slicing 'text' variable and finding from there
line 4 finds 'f' in 'text' as is
"""

# 9 - six
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)

# 10 - one line to rule them all
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

# 12 - whether me 3
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

# 14 - Code Assumed!
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# result variable -> readability
result = zip(my_str, my_list, my_tuple, my_range)
print(list(result))