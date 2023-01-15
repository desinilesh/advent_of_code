INPUT = "input.txt"

def get_rates(numbers):
    gamma = []
    epsilon = []
    size = len(numbers)
    for i in range(len(numbers[0])):
        num_1s = sum([int(number[i]) for number in numbers])
        num_0s = size - num_1s
        gamma.append('1' if num_1s > num_0s else '0')
        epsilon.append('0' if num_1s > num_0s else '1')
    return int("".join(gamma), 2), int("".join(epsilon), 2)

with open(INPUT, "r") as f:
    data = f.readlines()

numbers = []
for line in data:
    number = [char for char in line.strip()]
    numbers.append(number)
gamma, epsilon = get_rates(numbers)
print(f"Power consumption = {gamma * epsilon}")
