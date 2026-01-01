import sys

sys.stdin = open('1/1in.txt', 'r')
N = 4777
curr = 50
count = 0

for _ in range(N):
    str = input().strip()
    num = int(str[1:])
    direction = str[0]
    #print(curr)
    
    if direction == 'L': # minus
        curr -= num
    else:
        curr += num
    curr = curr % 100
    if curr % 100 == 0:
        count += 1

print(f"ans = {count}")

