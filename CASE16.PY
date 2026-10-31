capacity = 1000
water = 500

inflow = [200, 300, 100, 250]
outflow = [100, 150, 200, 100]

for day in range(len(inflow)):
    water = water + inflow[day] - outflow[day]

    if water > capacity:
        print("Day", day + 1, "- Overflow")
        water = capacity
    elif water < 0:
        print("Day", day + 1, "- Water shortage")
        water = 0

    print("Day", day + 1, "Water level:", water)