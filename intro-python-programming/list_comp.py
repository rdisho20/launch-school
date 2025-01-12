# transformation
squares = [number * number for number in range(5)]
print(squares)

# selection
multiples_of_6 = [number for number in range(20)
                  if number % 6 == 0]
print(multiples_of_6)

# transformation & selection
even_squares = [ number * number
                 for number in range(10)
                 if number % 2 == 0 ]
print(even_squares)

# --------------------
cats_colors = {
    'Tess': 'brown',
    'Leo': 'orange',
    'Fluffy': 'gray',
    'Ben': 'black',
    'Kat': 'orange',
}

names = [ name.upper() for name in cats_colors ]
print(names)
# OR limiting to 'orange' cats:
names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange' ]
print(names)
# OR multiple selection criteria
names = [ names.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L']
print(names)
