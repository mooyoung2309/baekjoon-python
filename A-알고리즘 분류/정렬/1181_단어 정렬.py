import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(str(input().strip()))
arr = list(set(arr))
arr.sort(key= lambda x : (len(x), x))

for val in arr:
    print(val)
