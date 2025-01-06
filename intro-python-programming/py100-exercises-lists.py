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