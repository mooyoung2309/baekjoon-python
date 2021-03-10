import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().split())
graph = collections.defaultdict(list)
indegree = [0 for i in range(N + 1)]
queue = collections.deque()
result = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    i = queue.popleft()
    result.append(i)
    for j in graph[i]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)

print(*result)
