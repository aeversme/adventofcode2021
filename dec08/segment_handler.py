"""
Segments:

  --s1--
|        |
s2      s3
|        |
  --s4--
|        |
s5      s6
|        |
  --s7--

"""

ALPHA = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# string(2) is at [0]
# string(3) is at [1]
# string(4) is at [2]
# string(6) are at [6], [7], and [8]


def segment_s5(input_list):
    global ALPHA
    print(input_list)
    # determine which string represents '9'
    index = 0
    for i in range(6, 9):
        count = 0
        for letter in input_list[2]:
            if letter in input_list[i]:
                count += 1
        if count == 4:
            index = i
            break
    print(f"list index {index} represents '9'")
    # determine which letter is not in string representing '9'
    s5 = ''
    for char in ALPHA:
        if char not in input_list[index]:
            print(f"{char} not in index {index}")
            s5 = char
    return s5
