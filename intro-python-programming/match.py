value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _: # default case
        print('value is neither 5 nor 6')

# functionally identical if/else
if value == 5:
    print('value is 5')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')

# using '|' to test against multiple values in single case
match value:
    case 1 | 2 | 3 | 4:
        print('value is < 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:
        print('value is not 1, 2, 3, 4, 5, or 6')