import sys

sys.stdin = open('2/2in.txt', 'r')
ranges = input().split(',')
print(ranges)
l = []
r = []
for s in ranges:
    x = s.split('-')
    l.append(int(x[0]))
    r.append(int(x[1]))

print(l)
print(r)
assert len(l) == len(r)

def invalid(a: str):
    return a[:len(a)//2] == a[len(a)//2:]
    #0-2 and 2-4

count = 0
for i in range(len(l)):
    for j in range(l[i], r[i] + 1):
        str_j = str(j)
        if len(str_j) % 2 == 0 and invalid(str_j):
            #print(count)
            count += j
print(f"ans: {count}")