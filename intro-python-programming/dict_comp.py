import pprint

squares = { f'{number}-squared': number * number
            for number in range(1,6) }
pprint.pprint(squares)

# Set compr. (single value -> exp., NOT key:value)
squares = { number * number for number in range(1, 6) }
pprint.pprint(squares)