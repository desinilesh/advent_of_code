INPUT = "input.txt"

def get_priority(common):
    if common.islower():
        return (ord(common) - ord('a') + 1)
    return (ord(common) - ord('A') + 27)

with open(INPUT, "r") as f:
    data = f.readlines()

sum_of_priorities = 0
for i in range(0, len(data), 3):
    badge = (set(data[i].strip()) &
             set(data[i + 1].strip()) &
             set(data[i + 2].strip())).pop()
    sum_of_priorities += get_priority(badge)

print(f"[PART 2] Sum of badge priorities = {sum_of_priorities}")
