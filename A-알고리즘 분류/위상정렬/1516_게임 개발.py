import sys
import collections

input = sys.stdin.readline

N = int(input())
times = [0 for _ in range(N + 1)]
dp = [0 for _ in range(N + 1)]
inDegree = [0 for _ in range(N + 1)]
graph = collections.defaultdict(list)
for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]
    tmp = tmp[1:-1]
    for j in tmp:
        graph[j].append(i)
    inDegree[i] = (len(tmp))

queue = collections.deque()
for i in range(1, N + 1):
    if inDegree[i] == 0:
        queue.append(i)
        dp[i] = times[i]

while queue:
    node = queue.popleft()
    for i in graph[node]:
        inDegree[i] -= 1
        dp[i] = max(dp[node] + times[i], dp[i])
        if inDegree[i] == 0:
            queue.append(i)

for i in range(1, N + 1):
    print(dp[i])