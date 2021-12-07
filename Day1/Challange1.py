depths = []

with open('/Users/mark/Projects/AoC2021/Day1/input.txt') as f:
    depths = [int(x.strip()) for x in f.readlines()]

depthCount = 0
lastDepth = 0
firstDepth = True

for depth in depths:
    if firstDepth:
        lastDepth = depth
        firstDepth = False

    diff = depth - lastDepth
    lastDepth = depth

    if diff > 0:
        depthCount+=1

print(depthCount)