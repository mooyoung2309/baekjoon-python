import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

total_cnt = 0
for n in nums:
    if n <= 1:
        continue
    cnt = 0
    for i in range(2, n):
        if n % i == 0:
            cnt += 1
    if cnt == 0:
        total_cnt += 1
print(total_cnt)