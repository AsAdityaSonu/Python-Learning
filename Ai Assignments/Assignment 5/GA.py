import math as m

initial = [[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]
wt = [45, 40, 50, 90]
val = [3, 5, 8, 10]
capacity = 100

def fitness(initial, sorted_list, capacity):
    for i in range(len(sorted_list)):
        if sorted_list[i][1] > capacity:
            sorted_list.pop(i)  
    print(sorted_list)

def value(initial, wt, val):
    ans = []
    for i in range(4):
        l = []
        l.append(i)
        summ = 0
        for j in range(4):
            if initial[i][j] == 1:
                summ = summ + wt[j]
        l.append(summ)

        summ = 0
        for j in range(4):
            if initial[i][j] == 1:
                summ = summ + val[j]
        l.append(summ)

        ans.append(l)

    return ans


def crossOver(c1, c2):
    mid = m.ceil(len(c1))
    new_c1 = c1[:mid] + c2[mid:]
    new_c2 = c2[:mid] + c1[mid:]

    return new_c1, new_c2



val_item = value(initial, wt, val)
print(val_item)

sorted_list = sorted(val_item, key=lambda x: x[1], reverse=True)
print(sorted_list)

initial[0], initial[1] = crossOver(initial[0], initial[1])

fitness(initial, sorted_list, capacity)

print(initial)
