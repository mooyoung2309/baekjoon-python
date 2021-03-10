import sys

input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.extend(list(map(int, input().split())))

dp = [0 for _ in range((N + 1)* N // 2) ]
dp[0] = graph[0]
sum = 0
for i in range(1, N):
    sum += i
    for j in range(sum, sum + i + 1):
        p1 = 0 if j == sum else dp[j - i - 1]
        p2 = 0 if j == sum + i else dp[j - i]

        dp[j] = max(p1, p2) + graph[j]

print(max(dp))