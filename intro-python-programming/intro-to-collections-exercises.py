# 2
stuff = ('hello', 'world', 'bye', 'now')
stuff_list = list(stuff)
stuff_list[2] = 'goodbye'
new_stuff = tuple(stuff_list)

print(new_stuff)

# 3 - list vs tuple
"""
differences: 
list is mutable, tuple is immutable
lists use surrounding '[]', tuples use surrounding '()'

similarities:
thus can access using indeces 'my_list[1]' / 'my_tuple[1]'
both maintain element order
"""

# 4 - strings
"""
mine: Strings are sequences because they are iterable
LS: ordered elements and can be indexed by whole numbers
"""

# 5 - set types vs sequence types
"""
sequence types are ordered elements and can be indexed by whole numbers
set types are unordered and cannot be indexed
"""

# 6 - convert pi
pi = 3.141592
str_pi = str(pi)
print(str_pi)

# 7 - ID range numbers
range(7) # 0, 1, 2, 3, 4, 5, 6
range(1, 6) # 1, 2, 3, 4, 5
range(3, 15, 4) # 3, 7, 11
range(3, 8, -1) # []
range(8, 3, -1) # 8, 7, 6, 5, 4

# 8 - print range
print(list(range(3, 17, 4)))

# 11 - name, country
country_dict = {
    'Alice':        'USA',
    'Francois':     'Canada',
    'Inti':         'Peru',
    'Monika':       'Germany',
    'Sanyu':        'Uganda',
    'Yoshitaka':    'Japan',
}

def which_country(str):
    print(country_dict[str])

which_country('Alice')
which_country('Sanyu')

