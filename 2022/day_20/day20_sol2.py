from collections import deque

INPUT = "input.txt"
DECRYPTION_KEY = 811589153
NUM_MIXES = 10

def mix(d: deque):
    """ Move each number once, using original indexes """
    num_elements = len(d)
    for original_index in range(num_elements):
        while d[0][0] != original_index: # Bring required element to the top left
            d.rotate(-1)

        current_tuple = d.popleft()
        n = current_tuple[1] % len(d) # retrieve the value to move by; allow for wrapping over
        d.rotate(-n) # rotate by n positions. (- indicates left->right shift, + indicates right->left shift)
        d.append(current_tuple) # Reinsert our tuple at the end
        # print(d)
    return d

def value_at_index(values: list, index: int):
    """ Determine the value at position index in our list.
    If index is beyond the end of the list, then wrap the values (as many times as needed). """
    position = (values.index(0) + index) % len(values)
    return values[position]

with open(INPUT, "r") as f:
    coordinates = list(map(int, f.read().splitlines()))

decrypted_coordinates = [DECRYPTION_KEY * value for value in coordinates]
# deque of tuple with original index and coordinates
d = deque(list(enumerate(decrypted_coordinates)))

for _ in range(NUM_MIXES):
    d = mix(d)

sum_of_coordinates = 0
for i in range(1000, 3001, 1000):
    sum_of_coordinates += value_at_index([val[1] for val in d], i)
print(f"[PART 2] Sum of decrypted coordinates at specific indices = {sum_of_coordinates}")
