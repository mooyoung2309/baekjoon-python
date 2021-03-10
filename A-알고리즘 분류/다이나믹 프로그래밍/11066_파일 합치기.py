import sys
import collections
from typing import List

input=sys.stdin.readline

def sum_file(K: int, nums: List[int]) -> int:
    dp = [[0]*K for _ in range(K)]
    print(dp)
    for i in range(K - 1):
        dp[i][i + 1] = nums[i] + nums[i + 1]
        for j in range(i+2, K):
            dp[i][j] = dp[i][j-1] + nums[j]
    print(dp)
    for d in range(2, K):
        for i in range(K-d):
            j = i+d
            minimum = [dp[i][k] + dp[k+1][j] for k in range(i, j)]
            print(minimum)
            dp[i][j] += min(minimum)
            print(dp)
    return 0

T = int(input())

for _ in range(T):
    K = int(input())
    nums = list(map(int, input().split()))
    sum_file(K, nums)