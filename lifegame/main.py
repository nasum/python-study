# ライフゲーム
import subprocess
import sys
from time import sleep


def living(matrix, x, y):
    max_x = len(matrix[0])
    max_y = len(matrix)

    if x < 0:
        return False
    elif x >= max_x:
        return False
    elif y < 0:
        return False
    elif y >= max_y:
        return False

    if matrix[y][x] == 1:
        return True
    else:
        return False


def next_live(matrix, x, y):
    living_cell_count = 0

    if living(matrix, x-1, y-1):
        living_cell_count += 1
    if living(matrix, x, y-1):
        living_cell_count += 1
    if living(matrix, x+1, y-1):
        living_cell_count += 1

    if living(matrix, x-1, y):
        living_cell_count += 1
    if living(matrix, x+1, y):
        living_cell_count += 1

    if living(matrix, x-1, y+1):
        living_cell_count += 1
    if living(matrix, x, y+1):
        living_cell_count += 1
    if living(matrix, x+1, y+1):
        living_cell_count += 1

    if living_cell_count == 3 and matrix[y][x] == 0:
        return True
    elif (living_cell_count == 2 or living_cell_count == 3) and matrix[y][x] == 1:
        return True
    elif living_cell_count <= 1 and matrix[y][x] == 1:
        return False
    elif living_cell_count >= 4 and matrix[y][x] == 1:
        return False


def run(matrix):
    subprocess.call(['clear'])
    # 新しいマトリックスを初期化
    new_matrix = [[0 for i in range(len(matrix[0]))]
                  for j in range(len(matrix))]

    for y, line in enumerate(matrix):
        for x, cell in enumerate(line):
            if next_live(matrix, x, y):
                new_matrix[y][x] = 1

    sys.stdout.write('\r\033[K')
    sys.stdout.flush()

    # マトリックスを表示
    for line in new_matrix:
        for cell in line:
            sys.stdout.write("■") if cell == 1 else sys.stdout.write("□")
        print()
    sleep(0.5)
    run(new_matrix)


# matrix = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [0, 0, 0]
# ]
# run(matrix)
