import sys

sys.stdin = open('11/11in.txt', 'r')

def solve(connections):
    # do DFS on the graph until 'out'
    count = 0
    stack = ['you']

    while stack:
        curr = stack.pop()
        if connections[curr] == {'out'}:
            count += 1
        else:
            for next in connections[curr]:
                stack.append(next)

    return count

connections = {}
paths = 0

while True:
    try:
        x = input().split()
        connections[x[0][:3]] = set(x[1:])        
    except EOFError:
        break

#print(connections)
paths = solve(connections)
print(paths)
