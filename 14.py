import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()


def print_rocks():
    for i in range(DR):
        for j in range(DC):
            if (i, j) in static_rocks:
                print("#", end="")
            elif (i, j) in rocks:
                print("O", end="")
            else:
                print(".", end="")
        print("")
    print("")


def run():
    # not optimal, it takes a long time to finish
    global rocks

    # north
    edge = [(-1, i) for i in range(DC)]
    for i in range(DR):
        for j in range(DC):
            if (i, j) in static_rocks:
                edge[j] = (i, j)
            elif (i, j) in rocks:
                edge[j] = (edge[j][0] + 1, j)
                rocks = [x if x != (i, j) else edge[j] for x in rocks]

    if step == 1:
        print(f'Result 1 is: {sum(DC - i[0] for i in rocks)}')

    # west
    edge = [(i, -1) for i in range(DR)]
    for i in range(DR):
        for j in range(DC):
            if (i, j) in static_rocks:
                edge[i] = (i, j)
            elif (i, j) in rocks:
                edge[i] = (i, edge[i][1] + 1)
                rocks = [x if x != (i, j) else edge[i] for x in rocks]

    # south
    edge = [(DC, i) for i in range(DC)]
    for i in range(DR - 1, -1, -1):
        for j in range(DC):
            if (i, j) in static_rocks:
                edge[j] = (i, j)
            elif (i, j) in rocks:
                edge[j] = (edge[j][0] - 1, j)
                rocks = [x if x != (i, j) else edge[j] for x in rocks]

    # east
    edge = [(i, DR) for i in range(DR)]
    for i in range(DR):
        for j in range(DC - 1, -1, -1):
            if (i, j) in static_rocks:
                edge[i] = (i, j)
            elif (i, j) in rocks:
                edge[i] = (i, edge[i][1] - 1)
                rocks = [x if x != (i, j) else edge[i] for x in rocks]


DR = len(lines)
DC = len(lines[0])
total_load = 0
rocks = [(d, e) for e in range(DC) for d in range(DR) if lines[d][e] == "O"]
static_rocks = [(d, e) for e in range(DC) for d in range(DR) if lines[d][e] == "#"]
start = {v: True for v in rocks}
iterations = [start]
step = 1

while True:
    run()
    rocks_after_cycle = {v: True for v in rocks}
    if rocks_after_cycle not in iterations:
        iterations.append(rocks_after_cycle)
    else:
        ind = iterations.index(rocks_after_cycle) + 1
        while 1000000000 % ind != 0:
            ind += 1
        print(f'Result 2 is: {sum(DC - i[0] for i in [b for b in iterations[ind].keys()])}')
        break
    step += 1
