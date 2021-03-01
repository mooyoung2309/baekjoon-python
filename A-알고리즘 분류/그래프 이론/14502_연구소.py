import sys
import copy
input = sys.stdin.readline
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def dfs(stack, shield):
    global count_shield
    graph_tmp_map = copy.deepcopy(graph_map)
    stack_tmp = copy.deepcopy(stack)
    count_virus = len(stack_tmp)
    for indx in shield:
        graph_tmp_map[indx[0]][indx[1]] = 1

    while stack_tmp:
        node = stack_tmp.pop()
        ci, cj = node[0], node[1]
        for i in range(4):
            ni, nj = ci + di[i], cj + dj[i]
            if 0 <= ni < N and 0 <= nj < M and graph_tmp_map[ni][nj] == 0:
                graph_tmp_map[ni][nj] = 2
                stack_tmp.append([ni, nj])
                count_virus += 1

    # print("+++++++++++++++++++++++")
    # for i in range(len(graph_tmp_map)):
    #     print(graph_tmp_map[i])
    count_safe = len(graph_tmp_map) * len(graph_tmp_map[0])
    count_safe -= count_virus + len(shield) + count_shield
    return count_safe

def searchBf(arr, stack):
    len_arr = len(arr)
    max_safe = -sys.maxsize
    for i in range(0, len_arr):
        for j in range(i+1, len_arr):
            for k in range(j+1, len_arr):
                # print([arr[i], arr[j], arr[k]])
                max_safe = max(max_safe, dfs(stack, [arr[i], arr[j], arr[k]]))

    return max_safe

N, M = map(int, input().split())
graph_map = []
for _ in range(N):
    graph_map.append(list(map(int, input().split())))

#빈 칸의 인덱스, 바이러스 인덱스 저장
arr_empty = []
stack = []
count_shield = 0
for i in range(len(graph_map)):
    for j in range(len(graph_map[0])):
        if graph_map[i][j] == 0:
            arr_empty.append([i, j])
        elif graph_map[i][j] == 2:
            stack.append([i,j])
        else:
            count_shield += 1

print(searchBf(arr_empty, stack))
