import os
import down

with open(os.path.basename(__file__).split('.')[0] + '.txt', 'r') as f:
    lines = f.read().splitlines()


def compute(nums):
    if all(n == 0 for n in nums):
        return 0
    return nums[-1] + compute([nums[i+1]-nums[i] for i in range(len(nums)-1)])


def compute2(nums):
    if all(n == 0 for n in nums):
        return 0
    return nums[0] - compute2([nums[i+1]-nums[i] for i in range(len(nums)-1)])


res1 = 0
res2 = 0
for line in lines:
    numbers = [int(x) for x in line.split()]
    res1 += compute(numbers)
    res2 += compute2(numbers)

print(f'Result 1 is: {res1}')
print(f'Result 2 is: {res2}')
