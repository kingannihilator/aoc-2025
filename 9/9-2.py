# this is cheese

import sys
import numpy as np
import time
import matplotlib.pyplot as plt

start = time.time()

sys.stdin = open('9/9in.txt', 'r')

def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

tiles = []
while True:
    try:
        tiles.append(list(map(int, input().split(','))))
    except EOFError:
        break

x, y = zip(*tiles) # looks like an ellipse with a rectangle cut out in the middle
# plt.plot(x, y)
# plt.show()

def test():
    # area([94710, 50238], [4890, 67739]) # top left
    # area([94710, 48527], [3937,34256]) # top right
    return max(area([94710, 48527], [3937,34256]), area([94710, 50238], [4890, 67739]))


print(test())

'''
testing: 94710 50238
upper bound: y = 68128
            94774,68128
            94689,68128
top left corner: 4890,67739


testing: 94710 48527
lower bound: y = 33430
            94403,33430
            95484,33430
bottom left corner: 3937,34256
'''
