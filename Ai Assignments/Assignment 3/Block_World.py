import copy
import queue


def gen(state):
    l1 = []
    for i in range(len(state)):
        if len(state[i]) != 0:
            for j in range(len(state)):
                s1 = copy.deepcopy(state)
                if j != i:
                    x = s1[i][0]
                    s1[i].remove(x)
                    s1[j].insert(0, x)
                    l1.append(s1)
    return l1


# Fun1
def dfs(initial, goal):
    stack = [(initial, None)]
    visited = set()

    while stack:
        state, parent = stack.pop()
        visited.add(tuple(map(tuple, state)))

        if state == goal:
            path = []
            while parent is not None:
                path.append(state)
                state, parent = parent
            path.append(state)
            return path[::-1]

        for next_state in gen(state):
            if tuple(map(tuple, next_state)) not in visited:
                stack.append((next_state, (state, parent)))
    return None


# Fun 2
def bfs(s1, goal):
    open = []
    while (1):
        s = copy.deepcopy(s1)
        l = gen(s)
        for each in l:
            if each not in open:
                open.append(each)
                print(open)
        if len(open) > 0:
            s1 = open[0]
            del (open[0])
            print(s1)
            for each in s1:
                if each == goal:
                    print("found")
                    return
        else:
            print("not found")


def main():
    initial_state = [['A', 'B', 'C'], [], []]
    goal_state = [[], ['A', 'B', 'C'], []]

    path = dfs(initial_state, goal_state)
    if path is None:
        print("found.")
    else:
        for state in path:
            print(state)


if __name__ == "__main__":
    main()

# import copy
#
#
# def gen(state):
#     l1 = []
#     for i in range(len(state)):
#         if len(state[i]) != 0:
#             for j in range(len(state)):
#                 s1 = copy.deepcopy(state)
#                 if j != i:
#                     x = s1[i][0]
#                     # s1[i].remove(x)
#                     listx = list(s1[i])
#                     listx.remove(x)
#                     s1[i] = tuple(listx)
#
#                     s1[j].insert(0, x)
#                     l1.append(s1)
#     return l1
#
#
# def dfs(initial, goal):
#     stack = [(initial, None)]
#     visited = set()
#
#     while stack:
#         state, parent = stack.pop()
#         if state == goal:
#             path = []
#             while state is not None:
#                 path.append(state)
#                 state, parent = parent
#             return path[::-1]
#
#         visited.add(state)
#         for nextS in gen(state):
#             if nextS not in visited:
#                 stack.append((nextS, (state, parent)))
#     return None
#
#
# def main():
#     initial_state = (('A', 'B', 'C'), (), ())
#     goal_state = ((), ('A', 'B', 'C'), ())
#     path = dfs(initial_state, goal_state)
#     if path is None:
#         print("No solution found.")
#     else:
#         for state in path:
#             print(state)
#
#
# if __name__ == "__main__":
#     main()
