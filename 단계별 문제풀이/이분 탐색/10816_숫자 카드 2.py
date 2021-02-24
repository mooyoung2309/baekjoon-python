import sys
import collections
input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().split()))
nlist.sort()
M = int(input())
mlist = list(map(int, input().split()))

numlist = collections.defaultdict(int)
for num in nlist:
    numlist[num] += 1

for m in mlist:
    print(numlist[m])
