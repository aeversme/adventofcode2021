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

from input_handler import convert_for_part_two
import segment_handler as sh

with open('test_segment.txt') as s:
    segment = s.readlines()

segment_input, segment_output = convert_for_part_two(segment)

# print(segment_input)
# print(segment_output)

s5, nine_index = sh.segment_s5(segment_input[0])
print(f"segment s5: {s5}")
s1 = sh.segment_s1(segment_input[0])
print(f"segment s1: {s1}")
s7 = sh.segment_s7(segment_input[0], nine_index)
print(f"segment s7: {s7}")
s6, s3 = sh.segment_s6_s3(segment_input[0])
print(f"segment s6: {s6}")
print(f"segment s3: {s3}")
s2, s4 = sh.segment_s2_s4(segment_input[0], nine_index)
print(f"segment s2: {s2}")
print(f"segment s4: {s4}")
