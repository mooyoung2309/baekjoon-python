import sys
import copy
input = sys.stdin.readline

nums = list(map(int, input().split()))
asc = copy.deepcopy(nums)
asc.sort()
desc = copy.deepcopy(nums)
desc.sort()
desc.reverse()

if nums == asc:
    print('ascending')
elif nums == desc:
    print('descending')
else:
    print('mixed')
