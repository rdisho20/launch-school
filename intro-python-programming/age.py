current_age = int(input('How old are you? '))
years = [10, 20, 30, 40]

print(f"You are {current_age} years old.")

for i in range(4):
    print(f"In {years[i]} years, you will be {current_age + years[i]} years old.")

# just for loop -> display future ages
current_age = int(input('How old are you? '))

for future in range(10, 50, 10):
    print(f"In {future} years, you will be {current_age + future} years old.")