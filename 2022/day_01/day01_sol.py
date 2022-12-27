INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.readlines()

curr_elf = 0
elves = []
for line in data:
    if not line.strip():
        # Blank line
        elves.append(curr_elf)
        curr_elf = 0
        continue
    curr_elf += int(line.strip())
elves.append(curr_elf)

print(f"[PART 1] Total calories of elf with maximum load = {max(elves)}")
print(f"[PART 2] Total calories carried by top 3 elves = {sum(sorted(elves)[-3:])}")
