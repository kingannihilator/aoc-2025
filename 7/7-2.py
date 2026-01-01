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
arr.append(['^'] * len(arr[0]))
arr = np.pad(np.array(arr), pad_width=1, constant_values='.')
arr = arr.tolist()
arr[1][len(arr[0]) // 2] = '.'
arr[3][len(arr[0]) // 2] = '1'

total = 0
for row in range(len(arr)):
    for col in range(len(arr[0])):
        if arr[row][col] == '^':
            count = 0
            for i in range(row - 1, -1, -1):
                if arr[i][col] != '.':
                    break
                if arr[i][col - 1] != '.':
                    count += int(arr[i][col - 1])
                if arr[i][col + 1] != '.':
                    count += int(arr[i][col + 1])
            
            arr[row][col] = count
            if row == len(arr) - 2:
                total += count


print("total =", total)


'''

add lefts and rights up to the lowest middle

.......S.......
.......1.......
.......^.......
......1.1......
......^.^......
.....1.2.1.....
.....^.^.^.....
....1.3.3.1....
....^.^.^.^....


.......S.......
.......1.......
.......^.......
......1.1......
......^.^......
.....1.2.1.....
.....^.^.^.....
....1.3...1....
....^.^...^....
...1.4...1.1...
...^.^...^.^...
..1...4.....1..
..^...^.....^..
.1.1.4.7.0...1.
.^.^.^.^.^...^.
...............
1.2.0.1.1.211.1
   101111
3 + 32 + 5 = 40
'''