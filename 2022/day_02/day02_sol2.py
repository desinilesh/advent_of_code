INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.readlines()

total_points = 0
for line in data:
    opponent, outcome = line.split()
    opponent = ord(opponent) - ord('A') + 1
    if outcome == 'X':
        # Lose
        total_points += 0 + (3 if opponent == 1 else opponent - 1)
    elif outcome == 'Y':
        # Draw
        total_points += 3 + opponent
    else:
        # Win
        total_points += 6 + (1 if opponent == 3 else opponent + 1)

print(f"[PART 2]: Total Points = {total_points}")
