import time
import itertools as it

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

sum_button_presses = 0
for line in lines:
    parts = line.split(' ')
    lights_goal = [0 if p == '.' else 1 for p in parts[0][1:-1]]
    switch_options = [[int(n) for n in p[1:-1].split(',')] for p in parts[1:-1]]
    button_presses = 1
    while button_presses < len(switch_options):
        switch_combinations = it.combinations(switch_options, button_presses)
        found_switch_combination = False
        for switch_combination in switch_combinations:
            switch_presses = list(it.chain.from_iterable(switch_combination))
            lights_results = [switch_presses.count(i) % 2 for i,_ in enumerate(lights_goal)]
            if lights_results == lights_goal:
                found_switch_combination = True
                break
        if found_switch_combination:
            sum_button_presses += button_presses
            break
        button_presses += 1

print("Button presses part 1: %d" % sum_button_presses)
print("Time: %.6f" % (time.perf_counter() - start))




