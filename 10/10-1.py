import sys
from itertools import chain, combinations

sys.stdin = open('10/10in.txt', 'r')

def press(curr, b):
    for i in b:
        curr[i] = 0 if curr[i] == 1 else 1
    return curr

def solve(goal, buttons):
    print(goal, buttons)

    choices = chain.from_iterable(
        combinations(buttons, r) for r in range(len(buttons) + 1)
    ) #this is essentially breadth-first

    for pressed in choices:
        current = [0] * len(goal)
        #print(pressed)
        for but in pressed:
            current = press(current, but)

        if goal == current:
            print(pressed)
            return len(pressed)
    
ans = 0
while True:
    try:
        x = input().split()
        goal = list(x[0][1:-1])
        for i in range(len(goal)):
            if goal[i] == '.':
                goal[i] = 0
            else:
                goal[i] = 1
        buttons = x[1:-1]
        for i in range(len(buttons)):
            buttons[i] = list(map(int, buttons[i][1:-1].split(',')))
        ans += solve(goal, buttons)
    except EOFError:
        break

print(ans)