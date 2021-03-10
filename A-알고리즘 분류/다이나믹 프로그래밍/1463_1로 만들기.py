import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 0
dp[1] = 0

for i in range(2, N + 1):
    if i % 3 == 0 and dp[i//3] < dp[i-1]:
        dp[i] = dp[i//3] + 1
    elif i % 2 == 0 and dp[i//2] < dp[i-1]:
        dp[i] = dp[i//2] + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])