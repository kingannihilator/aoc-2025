import sys

sys.stdin = open('3/3in.txt', 'r')

def solve(string): 
    # find index l max value from 0:length - 1
    # find max value from i:length
    final = ""
    
    l = 0 #lower bound
    num = 11
    while num >= 0:
        max_l = string[l]
        for i in range(l, len(string) - num):
            if int(string[i]) > int(max_l):
                max_l = string[i]
                l = i
        final += max_l
        num -= 1
        l += 1
        #print(final)
    return int(final)


ans = 0
for _ in range(200):
    s = input().strip()
    ans += solve(s)
print(f"final answer: {ans}")
