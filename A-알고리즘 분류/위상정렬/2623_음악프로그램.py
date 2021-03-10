import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().split())
inDegree = [0 for _ in range(N + 1)]
graph = collections.defaultdict(list)
for _ in range(M):
    singer = list(map(int, input().split()))[1:]
    for i in range(1, len(singer)):
        graph[singer[i - 1]].append(singer[i])
        inDegree[singer[i]] += 1

queue = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)

result = []
while queue:
    node = queue.popleft()
    result.append(node)
    for i in graph[node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            queue.append(i)
if len(result) == N:
    print(*result)
else:
    print(0)
