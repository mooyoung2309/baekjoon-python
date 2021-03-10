import sys
import collections

input = sys.stdin.readline

N = int(input())
times = [0 for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]

graph = collections.defaultdict(list)
for i in range(1, N + 1):
    work = list(map(int, input().split()))
    times[i] = work[0]
    inDegree[i] += work[1]
    for j in work[2:]:
        graph[j].append(i)

queue = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        dp[i] = times[i]
        queue.append(i)

while queue:
    node = queue.popleft()

    for i in graph[node]:
        inDegree[i] -= 1
        dp[i] = max(dp[node] + times[i], dp[i])
        if inDegree[i] == 0:
            queue.append(i)

print(max(dp))
