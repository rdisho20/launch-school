# 1 - Loop and Print
for num in range(0, 11, 2):
    print(num)

# 2 - Countdown
for i in range(10, 0, -1):
    print(i)
print('Launch!')

# 3 - Triple Greeting
greeting = 'Aloha!'

for i in range(3):
    print(greeting)

# 4 - Take Two
for num in range(1, 101):
    print(num * 2)

# 5 - Looping over List Elements
lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

# 6 - Greet Your Friends
friends = ['Sarah', 'John', 'Hannah', 'Dave']

for friend in friends: # use 'friend' instead of 'name' to accurately describe loop
    print(f"Hello, {friend}!")

# 7 - Continue
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city == None:
        continue
    print(len(city))

# 8 - And on and on and on
count = 0

while count < 1:
    print('and on')
    count += 1

# 9 - Finding Nemo
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

# 10 - Loop on Command
while True:
    print('Should I stop looping?')
    answer = input()

    if answer == 'yes' or answer == 'YES':
        break