import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    res1 = 0

d = {i: 1 for i in range(1, len(lines)+1)}

for line in lines:
    game = int(line.split(":")[0].split()[1])
    win, my = line.split(":")[1].split(" | ")
    win = [int(x) for x in win.split()]
    my = [int(x) for x in my.split()]
    c = 0
    for i in win:
        if i in my:
            c += 1
            d[game + c] += d[game]
    if c == 1:
        res1 += 1
    elif c > 1:
        res1 += (2 ** (c - 1))
    game += 1

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {sum(d.values())}')
