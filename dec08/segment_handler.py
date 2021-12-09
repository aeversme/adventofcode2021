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

Using the sorted and ordered puzzle input, ex. ['be', 'bde', bceg', etc.], it is possible to determine the value of
each segment (one of the letters from a - g) by analyzing the strings of lengths 2, 3, 4, and the three strings of
length 6. These strings correspond to seven-segment displays of the integers '1', '7', '4', and some ordered
combination of '6', '9', or '0', respectively.

The segments are arbitrarily assigned variables s1 through s7 as seen in the above diagram.
"""


def segment_s5(input_list):
    """
    Takes a list of strings. Determines the input_list index of the string representing the number '9' on the display
    by comparing the three six-character strings against the four-character string '4'. Of the display numbers '6',
    '9', and '0', only '9' contains all of the same segments as '4'.

    The letter that is missing from string '9' corresponds to segment s5.

    Returns the letter for s5, and the index of string '9'.
    """

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(input_list)
    # determine index of string '9': must contain all letters of string '4'
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
    """
    Takes a list of strings. Determines which letter from string '7' is not also in string '4'. That letter
    corresponds to segment s1.

    Returns the letter for s1.
    """

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
    Takes a list of strings and an index. Determines which letter from strings '7' and '4' is not in string '9'
    (referenced using the index calculated in segment_s5()). That letter corresponds to segment s7.

    Returns the letter for s7.
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
    """
    Takes a list of strings. Determines which of the two letters from the string '1' is also in string '6', '9',
    and '0'. This common letter corresponds to segment s6. The other letter in string '1' corresponds to segment s3.

    Returns the letters for s6 and s3.
    """

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
    """
    Takes a list of strings and an index. Determines the index of string '0' by removing the index for string '9'
    from the list of possible indexes, and then checks which of the remaining strings contains both letters from
    string '1'.

    Determines which letter from string '4' is not in string '0'. This letter corresponds to segment s4.

    Determines which letter from string '4' is not in string '1' or s4. This letter corresponds to s2.

    Returns the letters for s4 and s2.
    """

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
