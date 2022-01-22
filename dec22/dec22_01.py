from input_handler import convert_input

with open('test-reboot.txt') as r:
    reboot_raw = r.readlines()

reboot_sequence = convert_input(reboot_raw)
print(reboot_sequence[:4])
