# 1 - Find string length
string1 = 'These aren\'t the droids you\'re looking for.'
print(len(string1))

# 2 - Upper case
string1 = 'confetti floating everywhere'
print(string1.upper())

# 3 - Ignoring Case
name = 'Roger'
string1 = 'RoGeR'
string2 = 'DAVE'

if name.casefold() == string1.casefold():
    print('true')
else:
    print('false')

if name == string2:
    print('true')
else:
    print('false')

# 4 - Multiline String
multi_line_string = """A pirate I was meant to be! 
Trim the sails and roam the sea!"""

print(multi_line_string)

# 5 - Contains Character
char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'
print(any([elem == 'x' for elem in char_sequence])) # using 'comprehension'

# 6 - Is Empty?
def is_empty(str):
    if len(str) == 0:
        return True
    else:
        return False

# 7 - Is Empty or Blank?
def is_empty_or_blank(string):
    if not string:
        return True
    elif all([elem == ' ' for elem in string]):
        return True 
    else:
        return False
    
"""LS
def is_empty_or_blank(s):
    return s.strip(' ') == ''

def is_empty_or_blank(s):
    return len(s.strip(' ')) == 0

Both solutions use s.strip(' ') -> remove leading & trailing spaces & check if result is empty.

Better:
def is_empty_or_blank(str):
    return not str or str.isspace()
"""
    
print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# 8 - capitalize
words = 'launch school tech & talk'

print(words.title())

# 9 - Check Prefix
def starts_with(string, prefix):
    return string.startswith(prefix)

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# 10 - Count Substrings
def count_substrings(string, substr):
    return string.count(substr)

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0