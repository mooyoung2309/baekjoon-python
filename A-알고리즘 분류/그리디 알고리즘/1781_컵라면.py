import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    a, b = map(int, input().split())
    graph.append((a, b))
graph.sort(key = lambda x : (x[0], -x[1]))

deadline = graph[0][0]
total = graph[0][1]
for i in range(1, N):
    if deadline == graph[i][0]:
        continue
    else:
        deadline = graph[i][0]
        total += graph[i][1]

print(total)