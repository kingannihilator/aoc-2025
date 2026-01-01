### unfinished (too slow)

import sys
import time

sys.stdin = open('11/11in.txt', 'r')
start = time.time()

def solve(connections):

    # do DFS on the graph until 'out'
    # keep track of if 'fft' and 'dac' have been seen
    count = 0
    stack = [('svr', False, False)] # seen_fft, seen_dac

    while stack:
        curr_node, seen_fft, seen_dac = stack.pop()
        # print(curr_node)1
        if curr_node == 'fft':
            seen_fft = not seen_fft
        elif curr_node == 'dac':
            seen_dac = not seen_dac

        if connections[curr_node] == {'out'}:
            if seen_dac and seen_fft:
                count += 1
        else:
            for next in connections[curr_node]:
                stack.append((next, seen_fft, seen_dac))

    return count

connections = {}
paths = 0

while True:
    try:
        x = input().split()
        connections[x[0][:3]] = set(x[1:])        
    except EOFError:
        break
    
# print(connections)
paths = solve(connections)
print(paths)
print(time.time() - start)