balance = ((((1000 * 1.05) * 1.05) * 1.05) * 1.05) * 1.05
print(f"single line expression for 'balance' result: {balance}")

balance2 = 1000 * 1.05
balance2 *= 1.05
balance2 *= 1.05
balance2 *= 1.05
balance2 *= 1.05

print(f"multi-line result w/ augmented expressions for 'balance2': {balance2}")