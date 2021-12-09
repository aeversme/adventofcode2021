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

with open('segment.txt') as s:
    segment = s.readlines()


def get_output_values():
    output_list = []
    segment_input, segment_output = convert_for_part_two(segment)

    for i in range(len(segment_input)):
        s5, nine_index = sh.segment_s5(segment_input[i])
        s1 = sh.segment_s1(segment_input[i])
        s7 = sh.segment_s7(segment_input[i], nine_index)
        s6, s3 = sh.segment_s6_s3(segment_input[i])
        s4, s2 = sh.segment_s2_s4(segment_input[i], nine_index)
        # print(f"s1: {s1}\ns2: {s2}\ns3: {s3}\ns4: {s4}\ns5: {s5}\ns6: {s6}\ns7: {s7}\n")

        decoder_dict = sh.segment_decoder(s1, s2, s3, s4, s5, s6, s7)

        # print(segment_output[i])
        output_number_string = ''
        for j in range(len(segment_output[i])):
            for key, value in decoder_dict.items():
                if segment_output[i][j] == value:
                    output_number_string += key
        output_list.append(int(output_number_string))

    # print(output_list)
    return output_list


outputs = get_output_values()
print(f"The sum of all the outputs is: {sum(outputs)}")
