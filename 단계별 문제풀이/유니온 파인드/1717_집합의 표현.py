import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]


def find(x):
    if x == parents[x]:
        return x
    else:
        y = find(parents[x])
        parents[x] = y
        return y


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x


for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
