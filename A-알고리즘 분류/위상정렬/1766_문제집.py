import sys
import heapq
import collections

input = sys.stdin.readline

N, M = map(int, input().split())
inDegree = [0 for _ in range(N + 1)]

graph = collections.defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

heap = []
for i in range(1, N + 1):
    if inDegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    node = heapq.heappop(heap)
    result.append(node)
    for i in graph[node]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(heap, i)
print(*result)

