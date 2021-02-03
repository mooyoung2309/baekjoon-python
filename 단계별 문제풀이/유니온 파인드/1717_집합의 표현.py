import collections
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
dic = collections.defaultdict(list)

for i in range(n+1):
    dic[i].append(i)
for _ in range(m):
    x, max, min = map(int, input().split())
    if min > max:
        max, min = min, max
    if x == 0:
        a = 0
        b = 0
        if min == max:
            continue
        for key, value in dic.items():
            if max in value:
                a = key
            if min in value:
                b = key
        if a < b:
            a, b = b, a
        dic[b].extend(dic[a])
        del(dic[a])
    elif x == 1:
        if max in dic[min]:
            print("YES")
        else:
            print("NO")


