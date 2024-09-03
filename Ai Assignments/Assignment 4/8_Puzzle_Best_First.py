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


def dequeue():
    global q
    global g
    global visited
    my_list = []
    for matrix in q:
        if matrix not in visited:
            my_list.append([heuristic(matrix, g), matrix])

    mylist = sorted(my_list)
    elem = mylist[0][1]
    q.remove(elem)
    visited.append(elem)
    return elem


def best_first_search(matrix, g):
    while True:
        new = move_up(matrix)
        if new != matrix:
            if new == g:
                print("found")
                print(matrix)
                return
            else:
                q = enqueue(new)

        new = move_down(matrix)
        if new != matrix:
            if new == g:
                print("found")
                print(matrix)
                return
            else:
                q = enqueue(new)

        new = move_right(matrix)
        if new != matrix:
            if new == g:
                print("Found")
                print(matrix)
                return
            else:
                q = enqueue(new)

        new = move_left(matrix)
        if new != matrix:
            if new == g:
                print("Found")
                print(matrix)
                return
            else:
                q = enqueue(new)

        if len(q) > 0:
            matrix = dequeue()
            print(matrix)
        else:
            print("not found")


q = []
mat = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
g = [[1, 2, 3], [8, 6, 4], [7, 0, 5]]
visited = []
pos = empty_tile(mat)

best_first_search(mat, g)
