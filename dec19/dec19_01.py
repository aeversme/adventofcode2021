from input_handler import convert_input
from beacon_handler import find_shared_beacons

with open('test-beacons.txt') as b:
    beacons_raw = b.readlines()

scanners = convert_input(beacons_raw)
print(f"There are {len(scanners)} scanners.")

# layer_1_list = []
#
# for i in range(1, len(scanners)):
#     print(f"Checking Scanner 0 and {scanners[i]}...")
#     diff_dict_filter, sum_dict_filter = find_shared_beacons(scanners[0], scanners[i])
#     if diff_dict_filter or sum_dict_filter:
#         print(f"=== Shared beacons found: {scanners[0]} and {scanners[i]}")
#         scanners[0].child_scanners.append(scanners[i])
#         scanners[i].parent_scanners.append(scanners[0])
#         layer_1_list.append(scanners[i])
#     else:
#         print(f"    No shared beacons found: {scanners[0]} and {scanners[i]}")
#
# print(f"Layer 1 scanners: {layer_1_list}")

diff_dict_filter, sum_dict_filter = find_shared_beacons(scanners[0], scanners[1])
print(diff_dict_filter)
print(sum_dict_filter)

# if shared_s1:
#     print(f"shared from scanner 1: {shared_s1}")
#     print(f"s1 shares {len(shared_s1)} beacons")
#     print(f"shared from scanner 2: {shared_s2}")
#     print(f"s2 shares {len(shared_s2)} beacons")
#     print(f"{shared_s1[0]} from {scanners[0]} shared with {shared_s1[0].shared_with}")
#
# for beacon in scanners[1].beacons:
#     if beacon.shared_with is None:
#         print(beacon)
