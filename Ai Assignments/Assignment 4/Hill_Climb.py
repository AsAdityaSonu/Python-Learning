import copy


def empty_tile(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                return [i, j]


def move_up(matrix):
    l = empty_tile(matrix)
    mat1 = copy.deepcopy(matrix)
    i = l[0]
    j = l[1]
    if i != 0:
        mat1[i][j], mat1[i - 1][j] = mat1[i - 1][j], mat1[i][j]
        return mat1
    else:
        return matrix


def move_down(matrix):
    l = empty_tile(matrix)
    mat1 = copy.deepcopy(matrix)
    i = l[0]
    j = l[1]
    if i != 2:
        mat1[i][j], mat1[i + 1][j] = mat1[i + 1][j], mat1[i][j]
        return mat1
    else:
        return matrix


def move_left(matrix):
    l = empty_tile(matrix)
    i = l[0]
    j = l[1]
    mat1 = copy.deepcopy(matrix)
    if j != 0:
        mat1[i][j], mat1[i][j - 1] = mat1[i][j - 1], mat1[i][j]
        return mat1
    else:
        return matrix


def move_right(matrix):
    l = empty_tile(matrix)
    mat1 = copy.deepcopy(matrix)
    i = l[0]
    j = l[1]
    if j != 2:
        mat1[i][j], mat1[i][j + 1] = mat1[i][j + 1], mat1[i][j]
        return mat1
    else:
        return matrix


def enqueue(s):
    global q
    q = q + [s]
    return q


def heuristic(matrix, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != goal[i][j]:
                count += 1
    return count


def best_successor(matrix, goal):
    successors = [move_up(matrix), move_down(matrix), move_left(matrix), move_right(matrix)]
    successors_with_scores = [(heuristic(succ, goal), succ) for succ in successors if succ != matrix]
    if successors_with_scores:
        successors_with_scores.sort()
        return successors_with_scores[0][1]
    return None


def hill_climbing(matrix, goal):
    current = matrix
    while True:
        successor = best_successor(current, goal)
        if successor is None:
            print("Local maximum reached.")
            return
        if successor == goal:
            print("Goal reached:")
            print(successor)
            return
        if heuristic(successor, goal) >= heuristic(current, goal):
            print("Stuck in local maximum.")
            return
        current = successor


q = []
mat = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
g = [[1, 2, 3], [8, 6, 4], [7, 0, 5]]
hill_climbing(mat, g)
