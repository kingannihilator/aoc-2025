import sys

sys.stdin = open('6/6in.txt', 'r')

lines = []
for _ in range(4): #4
    lines.append(list(input()))
operations = list(input())

for _ in lines:
    print(_)
print(operations)

def calc(nums, operation):
    if operation == "+":
        total = 0
        for num in nums:
            total += num
        return total
    else:
        total = 1
        for num in nums:
            total *= num
        return total

total = 0
nums = []
c = len(lines[0]) - 1
while c >= 0:
    nums.append(int(lines[0][c] + lines[1][c] + lines[2][c] + lines[3][c]))
    if operations[c] == "*" or operations[c] == "+":
        total += calc(nums, operations[c])
        print(nums)
        nums = []
        c -= 1
    c -= 1



print('total =', total)