import sys
input = sys.stdin.readline

N = int(input())
atm = [0]*N
atm = list(map(int, input().split()))
atm.sort()

dp = [0]*N
dp[0] = atm[0]
for i in range(1, N):
    dp[i] = dp[i-1] + atm[i]

print(sum(dp))