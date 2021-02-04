import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
start = 0
end = len(nums) - 1
count = 0
while start < end:
    if nums[start] + nums[end] < x:
        start += 1
    elif nums[start] + nums[end] > x:
        end -= 1
    else:
        start += 1
        end -= 1
        count += 1

print(count)
