import os
import down

d = {'one': 1,
     'two': 2,
     'three': 3,
     'four': 4,
     'five': 5,
     'six': 6,
     'seven': 7,
     'eight': 8,
     'nine': 9}

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()
    res1 = 0
    res2 = 0
    for line in lines:
        # 1. part
        i = 0
        left, right = '', ''
        while True:
            if not left and str.isdigit(line[i]):
                left = line[i]
            if not right and str.isdigit(line[-i-1]):
                right = line[-i-1]
            if left and right:
                res1 += int(left+right)
                break
            i += 1
        i = 0

        # 2. part
        left, right, ltemp, rtemp = '', '', '', ''
        while True:
            ltemp += line[i]
            rtemp = line[-i-1] + rtemp
            for a in d.keys():
                if not left and a in ltemp:
                    left = str(d[a])
                if not right and a in rtemp:
                    right = str(d[a])
            if not left and str.isdigit(line[i]):
                left = line[i]
            if not right and str.isdigit(line[-i - 1]):
                right = line[-i - 1]
            if left and right:
                res2 += int(left + right)
                break
            i += 1
    print(f'Result 1 is: {res1}')
    print(f'Result 2 is: {res2}')
