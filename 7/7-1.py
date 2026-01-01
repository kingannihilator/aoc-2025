import sys
import numpy as np

sys.stdin = open('7/7in.txt', 'r')

arr = []
while True:
    try:
        line = list(input())
        arr.append(line)
    except EOFError:
        break
arr = np.array(arr)
print(arr)

count = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] == '^':
            l = 0
            m = 0
            r = 0
            for i in range(row):
                if arr[i][col - 1] == '^':
                    l = i
                if arr[i][col] == '^':
                    m = i
                if arr[i][col + 1] == '^':
                    r = i
    
            if max(l, m, r) != m:
                count += 1

count += 1 #topmost

print(count)


'''

.^...
...^.
..^..
.....
..^..

'''