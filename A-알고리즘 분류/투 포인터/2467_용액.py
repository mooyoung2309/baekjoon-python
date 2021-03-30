import sys

input = sys.stdin.readline

N = int(input())
waters = list(map(int, input().split()))
# print(N, waters)
sum_waters = []

sp, ep = 0, len(waters) - 1
min_water = (waters[sp], waters[ep], sys.maxsize)
while sp < ep:
    sum_water = waters[sp] + waters[ep]
    if abs(sum_water) < min_water[2]:
        min_water = (waters[sp], waters[ep], abs(sum_water))
    if sum_water < 0:
        sp += 1
    elif sum_water > 0:
        ep -= 1
    else:
        break
print(min_water[0], min_water[1])
