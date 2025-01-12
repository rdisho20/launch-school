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
my_name = 'Captain Ruby'

my_input = input(f'Change the captain\'s 2nd name to...\n')

new_captain_name = ''

def captain_name(captain, new_name):
    global new_captain_name
    new_captain = captain.split()
    new_captain[1] = new_name
    new_captain_name = ' '.join(new_captain)

captain_name(my_name, my_input)
print(new_captain_name)

# LS Solutions
first_8 = 'Captain Ruby'[:8]                        # slicing
new_str = first_8 + 'Python'                        # concat
print(new_str)

all_words = 'Captain Ruby'.split(' ')               # split
first_word = all_words[0]
new_str = first_word + ' Python'                    # concat
print(new_str)

new_str = 'Captain Ruby'.replace('Ruby', 'Python')
print(new_str)
# all print 'Captain Python'

# 8 - Internationalization 1
def greet(string):
    match string:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Ola!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!

# 9 - Locale Part 1
def locale(string):
    match string:
        case 'en_US.UTF-8':
            return 'en'
        case 'en_GB.UTF-8':
            return 'en'
        case 'ko_KR.UTF-8':
            return 'ko'

print(locale('en_US.UTF-8'))      # en
print(locale('en_GB.UTF-8'))      # en
print(locale('ko_KR.UTF-16'))     # ko

# 10 - Locale Part 2
def extract_region(string):
    index = string.find('_')
    region_code = f'{string[index + 1]}{string[index + 2]}'
    return region_code


print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

# LS Solution
def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

# 11 - Internationalization 2
ISO_LOCALE = {
    'en': {
        'US': 'Hey!',
        'GB': 'Hello!',
        'AU': 'Howdy!',
    },
    'fr': {
        'FR': 'Salut!',
        'CA': 'Bonjour',
        'MA': 'Salut!',
    },
}

def local_greet(locale):
    locale_split = locale.split('_')
    country_greeting = ISO_LOCALE[f'{locale_split[0]}'][f'{locale_split[1][:2]}']
    return country_greeting


print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Bonjour!
print(local_greet('fr_MA.UTF-8'))       # Salut!

# LS Solution
def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)