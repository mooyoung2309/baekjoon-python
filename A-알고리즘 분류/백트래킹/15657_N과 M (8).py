import sys

input = sys.stdin.readline


def bt(t, result):
    if t == 0:
        print(*result)
        return

    for i in range(N):
        if not result or result[M - t - 1] <= nums[i]:
            bt(t - 1, result + [nums[i]])


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

bt(M, [])
