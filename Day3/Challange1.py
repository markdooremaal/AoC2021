from collections import Counter

with open('/Users/mark/Projects/AoC2021/Day3/input.txt') as f:
    data = f.read().splitlines()

theta = ''
epsilon = ''

for i in range(len(data[0])):
    common = Counter([x[i] for x in data])
    if common['0'] > common['1']:
        theta += '0'
        epsilon += '1'
    else:
        theta += '1'
        epsilon += '0'
print(int(theta, 2) * int(epsilon, 2))
