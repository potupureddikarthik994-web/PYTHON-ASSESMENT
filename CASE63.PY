products = ["Laptop", "Phone", "Tablet"]
old_prices = [50000, 20000, 15000]
new_prices = [55000, 18000, 16500]

for i in range(len(products)):
    change = new_prices[i] - old_prices[i]
    percentage = change / old_prices[i] * 100

    print("\nProduct:", products[i])
    print("Old Price:", old_prices[i])
    print("New Price:", new_prices[i])
    print("Change:", round(percentage, 2), "%")

    if percentage > 0:
        print("Price increased")
    elif percentage < 0:
        print("Price decreased")
    else:
        print("No price change")