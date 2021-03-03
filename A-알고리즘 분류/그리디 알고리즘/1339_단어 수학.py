import sys
import collections

input = sys.stdin.readline

stack = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
graph = collections.defaultdict(str)
alp = collections.defaultdict(list)
N = int(input())
arr = []
for i in range(N):
    tmp = input().strip()
    arr.append(tmp)
    for j in range(len(tmp) - 1, -1, -1):
        alp[len(tmp) - j].append(tmp[j])

for i in range(10, -1, -1):
    if i in alp:
        for x in alp[i]:
            if x not in graph:
                graph[x] = stack.pop()

sum = 0
for val in arr:
    toInt = ''
    for x in val:
        toInt += graph[x]
    sum += int(toInt)
print(sum)
