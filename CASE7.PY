products = ["Book", "Bag", "Pen"]
prices = [200, 800, 20]
quantities = [2, 1, 5]

total = 0

print("----- RETAIL BILL -----")

for i in range(len(products)):
    amount = prices[i] * quantities[i]
    print(products[i], "=", amount)
    total += amount

if total >= 1000:
    discount = total * 0.10
else:
    discount = total * 0.05

final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Bill:", final_amount)