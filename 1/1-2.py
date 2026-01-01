import sys

sys.stdin = open('1in.txt', 'r')
N = 4777
curr = 50
count = 0

def add(curr, num, direction):
    count = 0
    if direction == 'L': # minus
        if curr - num <= 0:
            count += (abs(num - curr) // 100) + 1
            if curr == 0:
                count -= 1
            print(f"- {num} + {(abs(num - curr) // 100) + 1}")
    else:
        if curr + num >= 100:
            count += ((num + curr) // 100)
            print(f"+ {num} + {((num + curr) // 100)}")
    return count
#print(add(0, 199, 'L'))
'''
curr = 2
R200 -> 2
R199 -> 2
R198 -> 2
R197 -> 1

L203 -> 3 = 201 = 2
L202 -> 3 = 200 = 2
L201 -> 2 = 199 = 1
L200 -> 2

curr = 0
R99 -> 0
R100 -> 1
R101 -> 1

curr = 99

L98 -> 0
L99 -> 1
L100 -> 1

'''


for _ in range(N):
    str = input().strip()
    num = int(str[1:])
    direction = str[0]
    print(curr)
    count += add(curr, num, direction)
    if direction == 'L': # minus
        curr -= num
    else:
        curr += num
    curr = curr % 100

print(f"ans = {count}")

