from input_handler import convert_input

with open('segment.txt') as s:
    segment = s.readlines()

segment_list = convert_input(segment)

output_list = [i[1].split(' ') for i in segment_list]

unique_segment_count = 0
for i in output_list:
    for j in i:
        if len(j) == 2 or len(j) == 3 or len(j) == 4 or len(j) == 7:
            unique_segment_count += 1

print(f"Unique segment count: {unique_segment_count}")
