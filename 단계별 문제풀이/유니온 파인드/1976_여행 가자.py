cities = int(input())
_ = int(input())
parent = {i:i for i in range(1, cities+1)}
def parent_find(x):
    if x == parent[x]:
        return x
    p = parent_find(parent[x])
    parent[x] = p
    return parent[x]

def union(x,y):
    x = parent_find(x)
    y = parent_find(y)
    if x != y:
        parent[y] = x

for y in range(1, cities+1):
    maps = list(map(int, input().split()))
    for x in range(1, len(maps)+1):
      # 갈 수 있는 도시라면, 전부 y 기준으로 맞춘다.
        if maps[x-1] == 1:
            union(y, x)

tour = list(map(int, input().split()))
result = set([parent_find(i) for i in tour])
if len(result) != 1:
    print("NO")
else:
    print("YES")