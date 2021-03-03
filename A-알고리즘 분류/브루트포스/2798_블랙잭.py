import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

gap = sys.maxsize
gap_val = 0
for i in range(0, N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            n = nums[i] + nums[j] + nums[k]
            if gap > abs(M - n) and n <= M:
                gap = abs(M - n)
                gap_val = n
print(gap_val)