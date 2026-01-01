import sys

sys.stdin = open('2/2in.txt', 'r')
ranges = input().split(',')
#print(ranges)
l = []
r = []
for s in ranges:
    x = s.split('-')
    l.append(int(x[0]))
    r.append(int(x[1]))

# print(l)
# print(r)
assert len(l) == len(r)

def invalid(a: str):
    length = len(a)
    for i in range(1, length//2 + 1):
        if length % i != 0:
            continue
        #print(a, i, length//i)
        for j in range(i, length - i + 1, i):
            #print(a[j-i:j], a[j:j+i])
            if a[j-i:j] != a[j:j+i]:
                break
        else:
            return True
    return False

count = 0
for i in range(len(l)):
    for j in range(l[i], r[i] + 1):
        str_j = str(j)
        if invalid(str_j):
            print(str_j, "is valid")
            count += j

print(f"ans: {count}")