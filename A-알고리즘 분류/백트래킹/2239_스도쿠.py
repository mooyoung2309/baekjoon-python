import sys

input = sys.stdin.readline

def make_candidate(pos):
    nums = [False] + [True for _ in range(9)]

    x = (pos[0] // 3) * 3
    y = (pos[1] // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if puzzle[i][j]:
                nums[puzzle[i][j]] = False
    for i in range(9):
        if puzzle[pos[0]][i]:
            nums


puzzle = []
zero_position = []
state = False

for i in range(9):
    row = list(map(int, list(input())))
    puzzle.append(row)
    for j in range(9):
        if not row[j]:
            zero_position.append([i, j])

