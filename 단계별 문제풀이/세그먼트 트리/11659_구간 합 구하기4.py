import sys

input=sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0 for i in range(N)]
dp[0] = nums[0]

for i in range(1, len(nums)):
    dp[i] = dp[i-1] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    i, j = i - 1, j - 1
    if i == 0:
        print(dp[j])
    else:
        print(dp[j] - dp[i-1])