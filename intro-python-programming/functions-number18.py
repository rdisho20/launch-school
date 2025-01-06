def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [0, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(r'"numbers_1": at least one') if any(remainders_3(numbers_1)) else print(r'"numbers_1": none')
print(r'"numbers_2": at least one') if any(remainders_3(numbers_2)) else print(r'"numbers_2": none')
print(r'"numbers_3": at least one') if any(remainders_3(numbers_3)) else print(r'"numbers_3": none')
print(r'"numbers_4": at least one') if any(remainders_3(numbers_4)) else print(r'"numbers_4": none')