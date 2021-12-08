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

# string '1' is at [0]
# string '7' is at [1]
# string '4' is at [2]
# string '6', '9', '0' are at [6], [7], [8]


def segment_s5(input_list):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(input_list)
    # determine index of string '9'
    # must contain all letters of string '4'
    index = 0
    for i in range(6, 9):
        count = 0
        for char in input_list[2]:
            if char in input_list[i]:
                count += 1
        if count == 4:
            index = i
            break
    # print(f"list index {index} represents '9'")
    # determine which letter is not in '9'
    s5 = ''
    for char in alpha:
        if char not in input_list[index]:
            # print(f"{char} not in '9': {input_list[index]}")
            s5 = char
    return s5, index


def segment_s1(input_list):
    # determine which letter from string '7' is not also in string '4'
    s1 = ''
    for char in input_list[1]:
        if char not in input_list[2]:
            # print(f"{char} not in '4': {input_list[2]}")
            s1 = char
            break
    return s1


def segment_s7(input_list, nine_index):
    """
    Takes a list of strings and an index. Returns the letter from the string at the given index that is not found in
    strings at index 1 or 2.
    """
    # determine which letter from string '7' and '4' is not also in string '9'
    s7 = ''
    for char in input_list[nine_index]:
        if char not in input_list[1] and char not in input_list[2]:
            # print(f"{char} not in '7': {input_list[1]} or '4': {input_list[2]}")
            s7 = char
            break
    return s7


def segment_s6_s3(input_list):
    # determine which letter from '1' is in '6', '9', and '0'
    s6 = ''
    s3 = ''
    for char in input_list[0]:
        if char in input_list[6] and char in input_list[7] and char in input_list[8]:
            # print(f"{char} in {input_list[6]} & {input_list[7]} & {input_list[8]}")
            s6 = char
        else:
            # print(f"{char} not in all of {input_list[6]} & {input_list[7]} & {input_list[8]}")
            s3 = char
    return s6, s3


def segment_s2_s4(input_list, nine_index):
    sixes = [6, 7, 8]
    s4 = ''
    s2 = ''
    # determine index of string '0'
    sixes.remove(nine_index)
    # print(sixes)
    index = 0
    for i in range(len(sixes)):
        count = 0
        for char in input_list[0]:
            if char in input_list[sixes[i]]:
                count += 1
        if count == 2:
            index = sixes[i]
    # print(f"list index {index} represents '0'")
    # determine which letter from '4' is not in '0'
    for char in input_list[2]:
        if char not in input_list[index]:
            # print(f"{char } not in '0': {input_list[index]}")
            s4 = char
    # determine which letter from '4' is not in '1' or s4
    for char in input_list[2]:
        if char not in input_list[0] and char != s4:
            s2 = char
    return s4, s2
