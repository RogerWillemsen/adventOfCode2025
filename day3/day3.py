import time

def get_max_two_digits(numbers):
    max_base = max(numbers[:-1])
    max_base_index = numbers.index(max_base)
    return max(numbers[max_base_index + 1:]) + max_base * 10

def get_max(numbers, digits):
    remaining_numbers = numbers[:] #copy
    value = 0
    for i in range(digits, 0, -1):
        upper_bound = None if i == 1 else (-i + 1)
        max_base = max(remaining_numbers[:upper_bound])
        max_base_index = remaining_numbers.index(max_base) + 1
        remaining_numbers = remaining_numbers[max_base_index:]
        value += max_base * 10**(i-1)
    return value

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()
total1, total2 = 0, 0

for line in lines:
    numbers = [int(x) for x in list(line)]
    total1 += get_max(numbers, 2)
    total2 += get_max(numbers, 12)

print("Total part 1: %d" % total1)
print("Total part 2: %d" % total2)
print("Time: %.6f" % (time.perf_counter() - start))
