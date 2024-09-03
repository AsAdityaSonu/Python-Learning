import copy

q = []


def empty_tile(mat):
    for i in range(3):
        for j in range(3):
            if mat[i][j] == 0:
                return ([i, j])


def move_up(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i = l[0]
    j = l[1]
    if i != 0:
        mat1[i][j], mat1[i - 1][j] = mat1[i - 1][j], mat1[i][j]
        return mat1
    else:
        return mat


def move_down(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i = l[0]
    j = l[1]
    if i != 2:
        mat1[i][j], mat1[i + 1][j] = mat1[i + 1][j], mat1[i][j]
        return mat1
    else:
        return mat


def move_left(mat):
    l = empty_tile(mat)
    i = l[0]
    j = l[1]
    mat1 = copy.deepcopy(mat)
    if j != 0:
        mat1[i][j], mat1[i][j - 1] = mat1[i][j - 1], mat1[i][j]
        return mat1
    else:
        return mat


def move_right(mat):
    l = empty_tile(mat)
    mat1 = copy.deepcopy(mat)
    i = l[0]
    j = l[1]
    if j != 2:
        mat1[i][j], mat1[i][j + 1] = mat1[i][j + 1], mat1[i][j]
        return mat1
    else:
        return mat


def enqueue(s):
    global q
    q = q + [s]
    return q


def dequeue():
    global q
    elem = q[0]
    del q[0]
    return (elem)


def search(mat, g):
    while (1):
        new = move_up(mat)
        if new != mat:
            if new == g:
                print("found")
                return
            else:
                q = enqueue(new)
                print(q[len(q) - 1])

        new = move_down(mat)
        if new != mat:
            if new == g:
                print("found")
                return
            else:
                q = enqueue(new)
                print(q[len(q) - 1])
        new = move_right(mat)
        if new != mat:
            if new == g:
                print("Found")
                return
            else:
                q = enqueue(new)
                print(q[len(q) - 1])
        new = move_left(mat)
        if new != mat:
            if new == g:
                print("Found")
                return
            else:
                q = enqueue(new)
                print(q[len(q) - 1])
        if len(q) > 0:
            mat = dequeue()
        else:
            print("not found")


mat = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
g = [[2, 8, 1], [7, 4, 3], [0, 6, 5]]
pos = empty_tile(mat)
search(mat, g)
