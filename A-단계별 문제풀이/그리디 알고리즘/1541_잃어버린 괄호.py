import sys
import re

input = sys.stdin.readline

num_total = input().split('-')
minus_sum = []

for i in num_total:
    cnt = 0
    tmp = i.split('+')
    for j in tmp:
        cnt += int(j)
    minus_sum.append(cnt)
sum = minus_sum[0]
for i in range(1, len(minus_sum)):
    sum -= minus_sum[i]
print(sum)
