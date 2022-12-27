INPUT = "input.txt"

def get_priority(common):
    if common.islower():
        return (ord(common) - ord('a') + 1)
    return (ord(common) - ord('A') + 27)

with open(INPUT, "r") as f:
    data = f.readlines()

sum_of_priorities = 0
for line in data:
    line = line.strip()
    mid = len(line)//2
    common_element = (set(line[:mid]) & set(line[mid:])).pop()
    sum_of_priorities += get_priority(common_element)

print(f"[PART 1] Sum of badge priorities = {sum_of_priorities}")
