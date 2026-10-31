categories = ["Hotel", "Food", "Transport"]
expenses = [200, 100, 50]

exchange_rate = 83
conversion_fee = 0.02
budget = 30000

total = 0

for i in range(len(categories)):
    rupees = expenses[i] * exchange_rate
    fee = rupees * conversion_fee
    cost = rupees + fee
    total += cost

    print(categories[i], "Cost:", round(cost, 2), "INR")

print("Total Expense:", round(total, 2), "INR")

if total <= budget:
    print("Within budget")
else:
    print("Budget exceeded")

print("Remaining Budget:", round(budget - total, 2), "INR")