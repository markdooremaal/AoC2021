data = []

with open('/Users/mark/Projects/AoC2021/Day2/input.txt') as f:
    data = [(x.split(" ")) for x in f.readlines()]

hPos = 0
vPos = 0

for input in data:
    if input[0] == 'forward':
        hPos+= int(input[1])
    if input[0] == 'up':
        vPos -= int(input[1])
    if input[0] == 'down':
        vPos += int(input[1])

print(hPos * vPos)