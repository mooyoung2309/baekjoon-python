import sys
input = sys.stdin.readline

chu_num = int(input())
chu = [0]
chu.extend(list(map(int, input().split())))

gooseul_num = int(input())
gooseul = list(map(int, input().split()))

knapsack = [[0 for _ in range(len(chu) + 1)] for _ in range(sum(chu) + 1)]

for i in range(1, sum(chu)):
    for j in range(1, len(chu)):
        w, v = chu[j], chu[j]
        if i < w:
            knapsack[i][j] = knapsack[i][j-1]
            print("안넣었어", knapsack[i][j])
        else:
            knapsack[i][j] = max(v + knapsack[i - w][j], knapsack[i][j-1])
            print("넣었어", knapsack[i][j])
        print(i,v, knapsack[i])

print(chu)
