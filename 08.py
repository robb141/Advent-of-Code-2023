import os
import down
from math import lcm

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

instructions = lines[0]
d = {}
for i in lines[2:]:
    splitted = i.replace('(', '').replace(')', '').replace(',', '').split()
    d[splitted[0]] = (splitted[2], splitted[3])

starters = [j for j in d.keys() if j.endswith('A')]

Z = []
for s in range(len(starters)):
    step = 1
    i = 0
    elem = starters[s]
    while True:
        if instructions[i] == 'L':
            elem = d[elem][0]
        else:
            elem = d[elem][1]
        if elem.endswith('Z'):
            Z.append(step)
            break
        step += 1
        i = (i+1) % len(instructions)


print(f'Result 1 is: {Z[starters.index("AAA")]}')
print(f'Result 2 is: {lcm(*Z)}')
