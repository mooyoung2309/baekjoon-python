import sys
input = sys.stdin.readline


def parent_find(x):
    if x == parent[x]:
        return x
    y = parent_find(parent[x])
    parent[x] = y
    return y

def union(x,y):
    x = parent_find(x)
    y = parent_find(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]

T = int(input())
for _ in range(T):
    F = int(input())
    parent = {}
    number = {}
    for _ in range(F):
        a, b = map(str, input().split())
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1
        union(a,b)
        print(number[parent_find(a)])