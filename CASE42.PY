marks = [
    [85, 90, 78],
    [72, 80, 88],
    [95, 92, 96]
]

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])
    print("Student", i + 1)
    print("Total Marks:", total)
    print("Average:", average)

for j in range(len(marks[0])):
    total = 0
    for i in range(len(marks)):
        total += marks[i][j]
    print("Subject", j + 1, "Average:",
          total / len(marks))