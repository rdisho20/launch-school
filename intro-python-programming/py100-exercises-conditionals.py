# 1 Truthy vs. Falsy
"""
Falsy:
[]
0
None
False
"""

# 2 - Yes? No? Pt 1
import random
random_number = random.randint(0, 1)
print(f'current random number: {random_number}')
if random_number == 1:
    print('Yes!')
else:
    print('No.')