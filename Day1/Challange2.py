depths = []
rollingWindow = []

with open('/Users/mark/Projects/AoC2021/Day1/input.txt') as f:
    depths = [int(x.strip()) for x in f.readlines()]

for i in range(len(depths) - 2):
    rollingWindow.append(depths[i] + depths[i+1] + depths[i+2])

depthCount = 0
lastDepth = 0
firstDepth = True

for depth in rollingWindow:
    if firstDepth:
        lastDepth = depth
        firstDepth = False

    diff = depth - lastDepth
    lastDepth = depth

    if diff > 0:
        depthCount+=1

print(depthCount)