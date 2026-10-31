capacity = 50
passengers = 0

stops = [1, 2, 3, 4]
boarding = [15, 20, 10, 8]
alighting = [0, 5, 12, 3]

for i in range(len(stops)):
    passengers += boarding[i]
    passengers -= alighting[i]

    print("Stop:", stops[i])
    print("Passengers:", passengers)

    if passengers > capacity:
        print("Capacity exceeded")
    else:
        print("Within capacity")