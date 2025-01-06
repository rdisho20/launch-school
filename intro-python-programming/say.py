def say():
    """
    docstring refrencable w/ REPL help() function
    """
    print('Output from say')

print('First')
say()
print('Last')

print('-' * 60)
print(say.__doc__)
print('-' * 60)