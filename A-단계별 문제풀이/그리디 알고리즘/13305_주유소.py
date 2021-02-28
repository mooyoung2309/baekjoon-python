import sys
input = sys.stdin.readline

N = int(input())
doro = list(map(int, input().split()))
juyouso = list(map(int, input().split()))
min_value = sys.maxsize
sum = 0

for i in range(N-1):
    if i == 0:
        sum += juyouso[0] * doro[0]
        min_value = min(min_value, juyouso[0])
    else:
        min_value = min(min_value, juyouso[i])
        sum += min_value * doro[i]
print(sum)