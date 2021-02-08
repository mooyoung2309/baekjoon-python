import sys

input = sys.stdin.readline

N = int(input())
podo = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    podo[i] = int(input())
    if i < 3:
        dp[i] = sum(podo)
    else:
        temp = []
        temp.append(dp[i-3] + podo[i-1] + podo[i])
        temp.append(dp[i-2] + podo[i])
        temp.append(dp[i-1])
        dp[i] = max(temp)

print(dp[-1])