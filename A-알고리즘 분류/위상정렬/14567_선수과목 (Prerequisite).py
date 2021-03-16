import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().split())
inDegree = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]

graph = collections.defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    inDegree[B] += 1

queue = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i] = 1

while queue:
    node = queue.popleft()
    for i in graph[node]:
        inDegree[i] -= 1
        dp[i] = max(dp[node] + 1, dp[i])
        if inDegree[i] == 0:
            queue.append(i)

print(*dp[1:])
