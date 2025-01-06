# 1 - Multiply
def multiply(num1, num2):
    return num1 * num2

multiply(12, 4)

# 2 - Print Quote
def bruce_eckel_quote():
    print('Python is executable pseudocode.')

bruce_eckel_quote()

# 3 - Cite the Author
def cite(author, quote):
    print (f'{author} said: {quote}')

cite('Bruce Eckel', 'Python is executable pseudocode.')

# 4 - Squared Number
def squared_number(num):
    return num**2

squared_number(3)

#5 - Display Division
# no output

#6 - Three-way Comparison
def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    elif len(str1) == len(str2):
        return 0
    
print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity'))      #  1
print(compare_by_length('humor', 'grace'))           #  0

# 7 - Transformation
