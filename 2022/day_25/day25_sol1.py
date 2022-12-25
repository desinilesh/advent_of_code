from collections import deque

INPUT = "input.txt"

def snafu_2_decimal(num):
    SNAFU_2_DECIMAL = {
        '0':  0,
        '1':  1,
        '2':  2,
        '-': -1,
        '=': -2
    }
    value = 0
    for i, digit in enumerate(num[::-1]):
        value += SNAFU_2_DECIMAL[digit] * (5 ** i)
    return value

def get_total_value(data):
    total = 0
    for line in data:
        total += snafu_2_decimal(line.rstrip())
    return total

def decimal_2_snafu(dec_num):
    d = deque()
    while dec_num:
        rem = dec_num % 5
        dec_num //= 5

        if rem <= 2:
            d.appendleft(str(rem))
        elif rem == 3:
            d.appendleft('=')
            dec_num += 1
        else:
            d.appendleft('-')
            dec_num += 1
    return "".join(d)

with open(INPUT, "r") as f:
    data = f.readlines()

total = get_total_value(data)
total_snafu = decimal_2_snafu(total)
print(total_snafu)
