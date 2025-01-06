current_age = int(input('How old are you? '))
years = [10, 20, 30, 40]

print(f"You are {current_age} years old.")

for i in range(4):
    print(f"In {years[i]} years, you will be {current_age + years[i]} years old.")
