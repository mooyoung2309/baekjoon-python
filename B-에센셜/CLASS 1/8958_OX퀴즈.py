import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    arr = str(input())
    cnt = 0
    sum = 0
    for i in arr:
        if i == 'O':
            cnt += 1
        else:
            cnt = 0
        sum += cnt
    print(sum)