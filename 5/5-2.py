import sys

sys.stdin = open('5/5in.txt', 'r')

fresh = []
while True:
    line = input()
    if line == "":
        break
    x = list(map(int, line.split('-')))
    fresh.append(x)


fresh.sort()
print(fresh)
ans = 0
curr = fresh[0][0]
maximum = fresh[0][1]
i = 0
while i < len(fresh) - 1:
    if fresh[i][1] >= fresh[i + 1][0]:
        maximum = max(maximum, fresh[i + 1][1])
    else:
        ans += maximum - curr + 1
        curr = fresh[i + 1][0]
        maximum = fresh[i + 1][1]
    i += 1
ans += maximum - curr + 1
print(ans)