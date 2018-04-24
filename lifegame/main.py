# ライフゲーム


def born():
    """
    誕生
    死んでいるセルに隣接する生きたセルがちょうど三つあれば、次の世代に生まれる
    """
    return True


def living():
    """
    生存
    生きているセルに隣接する生きたセルが二つか三つなら、次の世代で生き残る
    """
    return True


def depopulation():
    """
    過疎
    生きているセルに隣接する生きたセルが一つなら、死滅する
    """
    return True


def overcrowding():
    """
    過密
    生きているセルに隣接する生きたセルが4つ以上なら、死滅する
    """
    return True


rules = (born, living, depopulation, overcrowding)


def run(matrix):
    new_matrix = [[0 for i in range(len(matrix[0]))]
                  for j in range(len(matrix))]
    for line in new_matrix:
        for cell in line:
            print('■', end="") if cell == 1 else print('□', end="")
        print()


"""
matrix[y][x]
x: 行
y: 列
"""
matrix = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]

run(matrix)
