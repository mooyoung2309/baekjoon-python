import sys
import math

input = sys.stdin.readline

min, max = map(int, input().split())

num = [True] * (max - min + 1)
count = 0
x = 1

while x * x <= max:
    x += 1
    sqr = x * x
    i = min // sqr

    while sqr * i <= max:
        idx = sqr * i - min

        if idx >= 0 and num[idx]:
            count += 1
            num[idx] = False
        i += 1

print(len(num) - count)