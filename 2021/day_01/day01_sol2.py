INPUT = "input.txt"
N = 3 # Number of elements in sliding window

with open(INPUT, "r") as f:
    data = f.readlines()

depths = []
for line in data:
    depths.append(int(line.strip()))

m = 0
for i in range(len(depths)):
    if i < N:
        continue
    if sum(depths[i - N:i]) < sum(depths[i - N + 1:i + 1]):
        m += 1
print(f"Number of measurements using {N}-measurement sliding window larger than previous measurement = {m}")
