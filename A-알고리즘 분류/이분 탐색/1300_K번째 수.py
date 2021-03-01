import sys
import collections
input = sys.stdin.readline

N = int(input())
K = int(input())

B = []

for i in range(N):
    for j in range(N):
        B.append((i + 1) * (j + 1))
B.sort()
print(B[K - 1])