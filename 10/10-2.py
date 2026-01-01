### unfinished

import sys
from itertools import chain, combinations

sys.stdin = open('10/10in.txt', 'r')

def press(curr, b):
    for i in b:
        curr[i] += 1
    return curr

def solve(buttons, joltage):
    print(buttons, joltage)
    count = 0
    # 
    return 0


ans = 0
while True:
    try:
        x = input().split()

        buttons = x[1:-1]
        for i in range(len(buttons)):
            buttons[i] = list(map(int, buttons[i][1:-1].split(',')))
        joltage = list(map(int, x[-1][1:-1].split(',')))
        ans += solve(buttons, joltage)
    except EOFError:
        break

print(ans)