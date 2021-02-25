import sys
import copy
input = sys.stdin.readline

def queen(ci, cj, qnum, chess, qpos):
    def newChess(x, y, zchess):
        new_chess = copy.deepcopy(chess)
        new_chess[x][y] = 3
        for i in range(N):
            for j in range(N):
                if i == x or j == y or abs(i - j) == abs(x - y):
                    if new_chess[i][j] == 0:
                        new_chess[i][j] = 1
        return new_chess

    print("-----------------------")
    print(qnum)
    for i in range(len(chess)):
        print(chess[i])
    print("-----------------------")


    for i in range(ci, N):
        for j in range(cj, N):
            if chess[i][j] == 0: #0이면 가능 1이면 불가능.
                new_qpos = copy.deepcopy(qpos)
                new_qpos.append([i, j])
                new_qnum = copy.deepcopy(qnum)
                new_qnum += -1
                queen(i, j, new_qnum, newChess(i,j,chess), new_qpos)

N = int(input())
qpos = []
chess = [[0 for _ in range(N)] for __ in range(N)]
queen(0, 0, N, chess, qpos)