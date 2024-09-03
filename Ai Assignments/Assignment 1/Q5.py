D = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}
print(D)

D[6] = "Six"
print(D)

del D[2]
print(D)

if 6 in D:
    print("yesssss..")
else:
    print("noooooo....")


print(len(D))

sum_of_values = sum(value for value in D.values() if isinstance(value, int))
print("Sum of integer values in the dictionary:", sum_of_values)