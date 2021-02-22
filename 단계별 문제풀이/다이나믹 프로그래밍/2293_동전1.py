import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]
dongjun = []
for _ in range(n):
    dongjun.append(int(input()))
dongjun.sort()

for i in range(1, k+1):
    dp[i] = dp[i-1]