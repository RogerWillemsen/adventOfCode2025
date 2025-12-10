import time
import scipy as sc

with open('input.txt') as f:
    lines = f.read().splitlines()

start = time.perf_counter()

sum_button_presses = 0
for line in lines:
    parts = line.split(' ')
    switch_options = [[int(n) for n in p[1:-1].split(',')] for p in parts[1:-1]]
    joltage_goal = [int(p) for p in parts[-1][1:-1].split(',')]

    # Prepare for minimization
    c = [1] * len(switch_options)
    Aeq = []
    for i in range(len(joltage_goal)):
        Aeq.append([switch.count(i) for switch in switch_options])
    beq = joltage_goal
    integrality = [1] * len(switch_options)

    res = sc.optimize.linprog(c, A_eq=Aeq, b_eq=beq, integrality=integrality, method='highs')
    sum_button_presses += res.fun

print("Button presses part 2: %d" % sum_button_presses)
print("Time: %.6f" % (time.perf_counter() - start))




