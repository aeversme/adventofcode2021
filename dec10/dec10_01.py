from input_handler import convert_input

with open('test-navsyntax.txt') as n:
    nav_raw = n.readlines()

nav_syntax = convert_input(nav_raw)
print(nav_syntax)
