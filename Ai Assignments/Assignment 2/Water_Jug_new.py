from collections import deque


def BFS(jug1, jug2, target):
    visited = {}  # map
    is_solved = False
    path = []

    q = deque()
    q.append((0, 0))  # pehle toh khali hi hoga na yrr 😮‍💨

    while len(q) > 0:
        u, v = q.popleft()

        if (u, v) in visited:
            continue

        if u > jug1 or v > jug2 or u < 0 or v < 0:
            continue

        path.append((u, v))
        visited[(u, v)] = 1  # yaha apan ja chuke, gud job

        # check karne ka re deva
        if u == target or v == target:
            is_solved = True
            if u == target:
                if v != 0:
                    path.append((u, 0))
            else:
                if u != 0:
                    path.append((0, v))

            for i in range(len(path)):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        # pani bharo (sab se bekar kam 😑)
        q.append((u, jug2))
        q.append((jug1, v))

        for ap in range(max(jug1, jug2) + 1):
            # jug2 ko jug1 mai dalo
            c = u + min(ap, v)
            d = v - min(ap, v)

            if c == jug1 or d == 0:
                q.append((c, d))

            # jug1 ko jug2 mai dalo
            c = u - min(ap, u)
            d = v + min(ap, u)

            if c == 0 or d == jug2:
                q.append((c, d))

        # sab khali karooooo..
        q.append((jug1, 0))
        q.append((0, jug2))

    if not is_solved:
        print("No solution")


def main():
    target = 2
    jug1, jug2 = 4, 3

    print("Steps: ")
    BFS(jug1, jug2, target)


main()