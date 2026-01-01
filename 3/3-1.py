import sys

sys.stdin = open('3/3in.txt', 'r')

def solve(string): 
    # find index l max value from 0:length - 1
    # find max value from i:length
    l = 0
    max_l = string[0]
    for i in range(0, len(string) - 1):
        if int(string[i]) > int(max_l):
            max_l = string[i]
            l = i

    max_r = string[l + 1]
    for j in range(l + 1, len(string)):
        if int(string[j]) > int(max_r):
            max_r = string[j]
    print(int(max_l + max_r))
    return int(max_l + max_r)
ans = 0
for _ in range(200):
    s = input().strip()
    ans += solve(s)
print(ans)
