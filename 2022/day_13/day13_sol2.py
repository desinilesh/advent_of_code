import ast
import sys

from functools import cmp_to_key

INPUT = "input.txt"

# Return of negative values imply that it is the right order
def compare(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            # Both are ints
            return left - right
        else:
            # left is int, right is list
            return compare([left], right)
    elif isinstance(right, int):
        # left is list, right is int
        return compare(left, [right])

    # left and right are list
    for l, r in zip(left, right):
        cmp = compare(l, r)
        if cmp:
            return cmp
    return len(left) - len(right)

packets = []
with open(INPUT, "r") as f:
    data = f.readlines()

for line in data:
    if not line.strip():
        continue
    packets.append(ast.literal_eval(line.strip()))

div_2_packet = [[2]]
div_6_packet = [[6]]
packets.append(div_2_packet)
packets.append(div_6_packet)

sum_of_pair_indices = 0
packets.sort(key=cmp_to_key(compare))
index_div_2_packet = packets.index(div_2_packet)
index_div_6_packet = packets.index(div_6_packet)

print(f"Decoder key for distress signal = {(index_div_2_packet + 1) * (index_div_6_packet + 1)}")
