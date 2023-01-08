INPUT = "input.txt"
with open(INPUT, "r") as f:
    data = f.readlines()

prev = None
m = 0
for line in data:
    curr = int(line.strip())
    if prev is not None and curr > prev:
        m += 1
    prev = curr
print(f"Number of measurements larger than previous measurement = {m}")
