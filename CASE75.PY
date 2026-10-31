students = [
    ("101", "Ravi", 85, 90),
    ("102", "Sita", 78, 82),
    ("101", "Arun", 95, 88),
    ("104", "", 110, 75)
]

ids = []

for student in students:
    roll, name, marks, attendance = student

    print("\nStudent:", roll, name)

    if roll in ids:
        print("Error: Duplicate ID")
    else:
        ids.append(roll)

    if name == "":
        print("Error: Missing name")

    if marks < 0 or marks > 100:
        print("Error: Invalid marks")

    if attendance < 0 or attendance > 100:
        print("Error: Invalid attendance")

    if (name != "" and 0 <= marks <= 100
            and 0 <= attendance <= 100
            and roll not in ids[:-1]):
        print("Record is valid")