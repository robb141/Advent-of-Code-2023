import os
import re
from functools import reduce
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()

res1 = 0
res2 = 0
for line in lines:
    blue = max([int(i) for i in re.findall(r'(\d+) blue', line)])
    green = max([int(i) for i in re.findall(r'(\d+) green', line)])
    red = max([int(i) for i in re.findall(r'(\d+) red', line)])
    if red <= 12 and green <= 13 and blue <= 14:
        game = int(re.match(r'Game (\d+):', line)[1])
        res1 += game
    res2 += reduce((lambda x, y: x * y), [blue, green, red])

print(res1)
print(res2)
