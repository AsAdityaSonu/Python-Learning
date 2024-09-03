jug1, jug2 = 3, 4
target = 2

x = y = 0
print(x, y)
mini = min(jug1, jug2)

while x != target and y != target:
    if mini == jug1 and x == 0:
        x = jug1
    elif mini == jug2 and y == 0:
        y = jug2
    elif x > 0:
        if y < jug2:
            pour = min(x, jug2 - y)
            x -= pour
            y += pour
    else:
        x = jug1

    print(x, y)

    if x == target or y == target:
        break

