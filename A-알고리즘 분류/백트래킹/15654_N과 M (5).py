import sys

input = sys.stdin.readline

def bt(t:int, result:list, visited:list):
    if t == 0:
        print(*result)
        return
    for i in range(len(nums)):
        if i not in visited:
            bt(t-1, result + [nums[i]], visited + [i])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

bt(M, [], [])