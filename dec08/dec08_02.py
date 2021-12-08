from input_handler import convert_for_part_two

with open('test_segment.txt') as s:
    segment = s.readlines()

segment_input, segment_output = convert_for_part_two(segment)

print(segment_input)
print(segment_output)
