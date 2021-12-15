from input_handler import convert_input

with open('test-chiton.txt') as c:
    chiton_raw = c.readlines()


chiton_map = convert_input(chiton_raw)
print(chiton_map)

# can only move up, down, left, right
# start at 0,0; must get to max_x,max_y
# add up value at each position entered/moved to
# don't count starting position
# find path with lowest total value
# lowest path value in test-chiton = 40

# ideas:
# evaluate paths of x number of steps ahead of current position
# evaluation function will be recursive (?), and also have to keep track of paths of all evaluations in that step
# move to next value on lowest path and reevaluate
# shouldn't double back on itself
# movement function will be recursive?
# base case: if current position = end position
