# 1 - To what values do the following expressions evaluate?
False or (True and False) # False
True or (1 + 2) # True -short circuit-
(1 + 2) or True # 3 -short circuit-
True and (1 + 2) # 3 -last subexpression-
False and (1 + 2) # False
(1 + 2) and True # True -last subexpression-
(32 * 4) >= 129 # False
False != (not True) # False
True == 4 # False -True in binary is 1-
False == (847 == '847') # True

# 2
def even_or_odd(num):
    if int(num) % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd(int(input('Enter number to test whether even or odd: ')))

# 3
# 'Product2'
# product not found!

# 4 - Refactor statement
# return ('bar' if foo() else qux())
"""
if foo():
    return 'bar'
else:
    return qux()
"""

# 6 - All caps
def allcaps(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str

allcaps('hello world')
allcaps('goodbye')

# 7 - Checking integer
def number_range(num):
    match num:
        case n if n in range(51):
            print(f'{num} is between 0 and 50')
        case n if n in range(51,101):
            print(f'{num} is between 51 and 100')
        case n if n > 100:
            print(f'{num} is greater than 100')
        case n if n < 0:
            print(f'{num} is less than 0')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0
            
