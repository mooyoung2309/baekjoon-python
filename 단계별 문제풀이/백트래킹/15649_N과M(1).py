from typing import List

N,M = map(int,input().split())
nums = []
def dfs(nums: List[int]):
    if(len(nums) == M):
        print(*nums)
    for i in range(1, N+1):
        next_nums = nums[:]
        if i in nums:
            continue
        next_nums.append(i)
        #print(next_nums)
        dfs(next_nums)

dfs(nums)
