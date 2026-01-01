import sys

sys.stdin = open('6/6in.txt', 'r')


nums = list(map(int, input().strip().split()))
columns = []
for i in range(len(nums)):
    columns.append([nums[i]])


for _ in range(3): #2 or 3
    nums = list(map(int, input().strip().split()))
    for i in range(len(nums)):
        columns[i].append(nums[i])
print(columns)
operations = list(input().strip().split())
print(operations)

total = 0
for i in range(len(columns)):
    if operations[i] == "+":
        for num in columns[i]:
            total += num
    else:
        product = 1
        for num in columns[i]:
            product *= num
        total += product
    
print(total)