import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    R, S = input().split()
    R = int(R)
    for x in S:
        for i in range(R):
            print(x, end='')
    print()