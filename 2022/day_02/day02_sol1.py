INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.readlines()

total_points = 0
for line in data:
    opponent, you = line.split()
    opponent = ord(opponent) - ord('A') + 1
    you = ord(you) - ord('X') + 1
    total_points += you
    if opponent == you:
        total_points += 3
    elif (opponent == you - 1) or ((you == 1) and (opponent == 3)):
        total_points += 6

print(f"[PART 1]: Total Points = {total_points}")
