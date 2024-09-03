import copy
import math


def empty(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == 0:
                return i, j


def up(A, i, j):
    if i == 0:
        # print(i, j)
        return A, i, j
    else:
        A[i][j], A[i - 1][j] = A[i - 1][j], A[i][j]
        # print(i - 1, j)
        return A, i - 1, j


def down(A, i, j):
    if i == len(A) - 1:
        # print(i, j)
        return A, i, j
    else:
        A[i][j], A[i + 1][j] = A[i + 1][j], A[i][j]
        # print(i + 1, j)
        return A, i + 1, j


def left(A, i, j):
    if j == 0:
        # print(i, j)
        return A, i, j
    else:
        A[i][j], A[i][j - 1] = A[i][j - 1], A[i][j]
        # print(i, j - 1)
        return A, i, j - 1


def right(A, i, j):
    if j == len(A[i]) - 1:
        # print(i, j)
        return A, i, j
    else:
        A[i][j], A[i][j + 1] = A[i][j + 1], A[i][j]
        # print(i, j + 1)
        return A, i, j + 1


def next_step(A, final, i, j):
    tempUp = copy.deepcopy(A)
    tempDown = copy.deepcopy(A)
    tempLeft = copy.deepcopy(A)
    tempRight = copy.deepcopy(A)

    tempUp, _, _ = up(tempUp, i, j)
    tempDown, _, _ = down(tempDown, i, j)
    tempLeft, _, _ = left(tempLeft, i, j)
    tempRight, _, _ = right(tempRight, i, j)

    countUp = countDown = countLeft = countRight = 0

    for x in range(len(A)):
        for y in range(len(A[i])):
            if final[x][y] != tempUp[x][y]:
                countUp += 1
            if final[x][y] != tempDown[x][y]:
                countDown += 1
            if final[x][y] != tempLeft[x][y]:
                countLeft += 1
            if final[x][y] != tempRight[x][y]:
                countRight += 1

    if A == tempUp:
        countUp = math.inf
    if A == tempDown:
        countDown = math.inf
    if A == tempLeft:
        countLeft = math.inf
    if A == tempRight:
        countRight = math.inf

    print("\n")
    print(countUp, countDown, countLeft, countRight)

    if countUp < countDown and countUp < countLeft and countUp < countRight:
        return 1
    elif countDown < countUp and countDown < countRight and countDown < countLeft:
        return 2
    elif countLeft < countRight and countLeft < countUp and countLeft < countDown:
        return 3
    elif countRight < countLeft and countRight < countUp and countRight < countDown:
        return 4


def main():
    initial = [[1, 2, 3], [5, 6, 0], [7, 8, 4]]
    final = [[1, 2, 3], [5, 8, 6], [0, 7, 4]]
    i, j = empty(initial)

    visited_states = set()
    while True:
        current_state_tuple = tuple(map(tuple, initial))
        # print(current_state_tuple)
        if current_state_tuple in visited_states:
            print("humse ni ho payegaaa... 😩")
            return

        visited_states.add(current_state_tuple)

        var = next_step(initial, final, i, j)
        if var == 1:
            initial, i, j = up(initial, i, j)
        elif var == 2:
            initial, i, j = down(initial, i, j)
        elif var == 3:
            initial, i, j = left(initial, i, j)
        elif var == 4:
            initial, i, j = right(initial, i, j)

        if initial == final:
            break

        # print("\n")
        # for row in initial:
        #     print(row)

    if initial == final:
        print("Goal ✅")
    else:
        print("No solution found.")

    print("\n")
    for f in final:
        print(f)


if __name__ == "__main__":
    main()

