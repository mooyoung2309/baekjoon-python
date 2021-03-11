import sys

input = sys.stdin.readline

def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]

def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    if x != y:
        parent[x] = y

G = int(input().split())
P = int(input().split())
plane = []
for _ in range(P):
    plane.append(int(input()))

parent = [i for i in range(G + 1)]
cnt = 0
for i in plane:
    x = parent_find(i)
    if x == 0:
        break
    union(x, x-1)
    cnt += 1

print(cnt)