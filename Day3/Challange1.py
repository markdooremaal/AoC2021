from collections import Counter

with open('/Users/mark/Projects/AoC2021/Day3/input.txt') as f:
    data = f.read().splitlines()

gamma = ''
epsilon = ''

for i in range(len(data[0])):
    common = Counter([x[i] for x in data])
    if common['0'] > common['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
print(int(gamma, 2) * int(epsilon, 2))
