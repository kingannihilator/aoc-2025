import sys
import math
import numpy as np

sys.stdin = open('8/8in.txt', 'r')

def distance(box1, box2):
    return math.sqrt((box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2)

boxes = []
while True:
    try:
        boxes.append(list(map(int, input().split(','))))
    except EOFError:
        break

distances = []
for i in range(len(boxes)):
    distances.append([])
    for j in range(i + 1):
        distances[i].append(np.inf)
    for j in range(i + 1, len(boxes)):
        distances[i].append(distance(boxes[i], boxes[j]))

distances = np.array(distances)

# print(distances)
# print(boxes)
circuits = []

while not (len(circuits) == 1 and len(circuits[0]) == len(boxes)): #repeat until one complete circuit
    r, c = map(int, np.unravel_index(np.argmin(distances), distances.shape))
    # print(circuits, r, c)
    to_merge = {r, c}
    non_merge = []
    for cir in circuits:
        if r in cir or c in cir:
            to_merge.update(cir)
        else:
            non_merge.append(cir)
    
    # print(to_merge)
    non_merge.append(to_merge)
    circuits = non_merge

    #print(circuits, r, c)

    distances[r, c] = np.inf

ans = boxes[r][0] * boxes[c][0]
print(ans)

