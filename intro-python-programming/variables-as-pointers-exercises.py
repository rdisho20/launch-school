# 5 - create deep copy
import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)

print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])
print()
"""All of the following should print True
because the elements are immutable
"""

print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])

# 6 - create shallow copy w/o 'copy' class
dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2)           # False
print(dict1['a']    is dict2['a'])      # True
print(dict1['a'][0] is dict2['a'][0])   # True
print(dict1['a'][1] is dict2['a'][1])   # True
print(dict1['b']    is dict2['b'])      # True
print(dict1['b'][0] is dict2['b'][0])   # True
print(dict1['b'][1] is dict2['b'][1])   # True