# 2 - Yes? No? Pt 1
import random
random_number = random.randint(0, 1)
print(f'current random number: {random_number}')
if random_number == 1:
    print('Yes!')
else:
    print('No.')

# 3 - Yes? No? Pt 2
import random
random_number = random.randint(0, 1)
print(f'current random number: {random_number}')
print("Yes!" if random_number == 1 else "No.")

# 4 - Check the Weather, Pt 1
weather = "sunny"
if weather == "sunny":
    print("It's a beautiful day!")
elif weather == "rainy":
    print("Grab your umbrella.")
else:
    print("Let's stay inside.")

# 5 - Match-Case
# prints "neigh"

# 6 - Check the Weather, Pt 2
weather = "snowy"
match weather:
    case "rainy":
        print("Grab your umbrella.")
    case "snowy":
        print("Do you wanna build a snowman?")
    case "sunny":
        print("It's a beautiful day!")
    case _:
        print("Let's stay inside.")

# 7
# "yes"
"""
The condition provided to our if statement uses the logical or operator, or. 
Therefore, the condition evaluates to a truthy value if either of its operands is truthy. 
Since True is truthy, the condition always evaluates as truthy.
"""

# 8
# "no"

# 9
# "$3.99"

# 10 - Are we moving?
# "Troooooo"