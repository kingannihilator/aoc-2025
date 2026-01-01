import sys

sys.stdin = open('5/5in.txt', 'r')

def valid(num):
    for range in fresh:
        if range[0] <= num and num <= range[1]:
            return 1
    return 0

fresh = []
while True:
    line = input()
    if line == "":
        break
    x = list(map(int, line.split('-')))
    fresh.append(x)

ans = 0
while True:
    try:
        id = int(input())
        ans += valid(id)
    except EOFError:
        break

print(ans)