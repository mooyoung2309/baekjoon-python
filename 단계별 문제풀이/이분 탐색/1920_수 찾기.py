from typing import List

N = int(input())
nlist = []
nlist = list(map(int, input().split()))
M = int(input())
mlist = []
mlist = list(map(int, input().split()))


def binary_search(target: int, list: List[int]):
    left = 0
    right = len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return 1
        elif list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


nlist.sort()
for i in mlist:
    print(binary_search(i, nlist))
