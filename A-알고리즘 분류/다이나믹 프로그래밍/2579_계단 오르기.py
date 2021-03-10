import sys
input = sys.stdin.readline

N = int(input())
num = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(N):
    num[i] = int(input())
dp[0] = num[0]
dp[1] = num[0] + num[1]
dp[2] = max(num[1] + num[2], num[0] + num[2])
for i in range(3, N):
    dp[i] = max(dp[i-3] + num[i] + num[i-1], dp[i-2] + num[i])

print(dp[N - 1])