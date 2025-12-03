import time
import math
import numpy as np

# If the repeating pattern is 42 and should be repeated 3 times to get to a number
# length of 6, this function will output 10101
def get_pattern_multiplier(number_length, repeating_length):
    repeat_powers = np.arange(0, number_length, repeating_length)
    repeat_multipliers = np.power(np.ones(repeat_powers.size) * 10, repeat_powers)
    return np.sum(repeat_multipliers)

# If a range consists of different lengths, it needs to be split
# For example, 95-101 becomes 95-99 and 100-101
def split_ranges_based_on_length(range_start, range_end):
    number_length_start = math.floor(math.log10(range_start)) + 1
    number_length_end = math.floor(math.log10(range_end)) + 1
    if number_length_start == number_length_end:
        return [(range_start, range_end)]
    return [(range_start, 10 ** number_length_start - 1), (10 ** number_length_start , range_end)]

def get_invalid_numbers_two_repeats(range_start, range_end):
    number_length = math.floor(math.log10(range_start)) + 1
    invalid = []

    for i in range(int(number_length/2)):
        repeating_length = i + 1
        if number_length / repeating_length == 2:
            invalid += get_invalid_numbers(range_start, range_end, number_length, repeating_length)

    return np.unique([x for x in invalid if range_start <= x <= range_end])

def get_invalid_numbers_any_repeats(range_start, range_end):
    number_length = math.floor(math.log10(range_start)) + 1
    invalid = []

    for i in range(int(number_length/2)):
        repeating_length = i + 1
        if number_length % repeating_length == 0:
            invalid += get_invalid_numbers(range_start, range_end, number_length, repeating_length)

    return np.unique([x for x in invalid if range_start <= x <= range_end])

def get_invalid_numbers(range_start, range_end, number_length, repeating_length):
    start_base = int(range_start / 10 ** (number_length - repeating_length))
    end_base = int(range_end / 10 ** (number_length - repeating_length)) + 1
    repeat_range = np.arange(start_base, end_base + 1)
    multiplier = get_pattern_multiplier(number_length, repeating_length)
    invalid_range = repeat_range * multiplier
    return invalid_range.tolist()

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()
line = lines[0]
total1, total2 = 0, 0

all_id_ranges = line.split(',')
for id_range in all_id_ranges:
    id_range_split = id_range.split('-')
    range_start = int(id_range_split[0])
    range_end = int(id_range_split[1])

    for split_range in split_ranges_based_on_length(range_start, range_end):
        invalid1 = get_invalid_numbers_two_repeats(split_range[0], split_range[1])
        invalid2 = get_invalid_numbers_any_repeats(split_range[0], split_range[1])
        total1 += sum(invalid1)
        total2 += sum(invalid2)

print("Total part 1: %d" % total1)
print("Total part 2: %d" % total2)
print("Time: %.6f" % (time.perf_counter() - start))
