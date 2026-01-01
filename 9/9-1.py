import sys

sys.stdin = open('9/9in.txt', 'r')

def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

tiles = []
while True:
    try:
        tiles.append(list(map(int, input().split(','))))
    except EOFError:
        break

print(tiles)
max_area = 0
for c1 in range(len(tiles)):
    for c2 in range(c1 + 1, len(tiles)):
        max_area = max(max_area, area(tiles[c1], tiles[c2]))
print(max_area)
