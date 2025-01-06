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
def is_empty_or_blank(str):
    if not str:
        return False
    if all([elem == ' ' for elem in str]):
        return True 
    else:
        return False