import sys
import numpy as np

sys.stdin = open('4/4in.txt', 'r')

arr = []
while True:
    try:
        arr.append(list(input()))
    except EOFError:
        break

arr = np.vstack(arr)
arr = np.pad(arr, pad_width=1, constant_values=".")

def surrounding_contains(arr, r, c, char):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            #print(r+i, c+j, arr[r + i][c + j], char)
            if arr[r + i][c + j] == char:
                #print("^ good")
                count += 1
    #print(count)
    if count < 4:
        return True
    return False

ans = 0
for r in range(1, len(arr) - 1):
    for c in range(1, len(arr[0]) - 1):
        if arr[r][c] == "@":
            if surrounding_contains(arr, r, c, "@"):
                ans += 1

print("final", ans)