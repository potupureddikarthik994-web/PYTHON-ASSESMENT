rows = 4
columns = 5
reserved_seat = (2, 3)

for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        if (i, j) == reserved_seat:
            print("R", end="\t")
        else:
            print("S", end="\t")
    print()