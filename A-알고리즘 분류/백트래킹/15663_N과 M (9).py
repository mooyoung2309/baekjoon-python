import sys
import copy

input = sys.stdin.readline


def bt(t, result_each, visited_each):
    if t == 0:
        if tuple(result_each) not in result_total:
            result_total.add(tuple(result_each))
            print(*result_each)
        return
    for i in range(N):
        if i not in visited_each:
            bt(t - 1, result_each + [nums[i]], visited_each + [i])


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result_total = set()
bt(M, [], [])
