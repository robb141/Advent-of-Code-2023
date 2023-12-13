import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    patterns = f.read().split('\n\n')
res1 = 0
res2 = 0


def compute(pat):
    DR = len(pat)
    for i in range(1, DR):
        if pat[i - 1] == pat[i]:
            flag = True
            row = 1
            while i + row < DR and i - 1 - row >= 0:
                if pat[i - 1 - row] != pat[i + row]:
                    flag = False
                    break
                row += 1
            if flag:
                return i
    return False


for lines in patterns:
    pattern = lines.split('\n')
    t = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
    temp_res = compute(t)
    if temp_res:
        res1 += temp_res
        continue
    temp = compute(pattern)
    res1 += (temp * 100)


def compute2(pat):
    DR = len(pat)
    for i in range(1, DR):
        smudges = sum(a != b for a, b in zip(pat[i - 1], pat[i]))
        if smudges < 2:
            flag = True
            row = 1
            while i + row < DR and i - 1 - row >= 0:
                if pat[i - 1 - row] != pat[i + row]:
                    smudges += sum(a != b for a, b in zip(pat[i - 1 - row], pat[i+row]))
                    if smudges > 1:
                        flag = False
                        break
                row += 1
            if flag and smudges == 1:
                return i
    return False


for lines in patterns:
    pattern = lines.split('\n')
    t = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
    temp_res = compute2(t)
    if temp_res:
        res2 += temp_res
        continue
    temp = compute2(pattern)
    res2 += (temp * 100)

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {res2}')
