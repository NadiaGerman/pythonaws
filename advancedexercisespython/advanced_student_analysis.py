# advanced_student_analysis.py

# list of students
students = [
    {"name": "Alice", "grades": [88, 92, 79]},
    {"name": "Bob", "grades": [90, 50]},
    {"name": "Charlie", "grades": [45, 30]},
    {"name": "David", "grades": []},  # no grades
    {"name": "Eva", "grades": [100, 95, 100]}
]

# 1. Calculate the average grade for each student
def calculate_average(student):
    grades = student["grades"]
    if grades:
        return sum(grades) / len(grades)
    else:
        return None

averages = list(map(lambda s: (s["name"], calculate_average(s)), students))
print("\n--- Student Averages ---")
for name, avg in averages:
    if avg is not None:
        print(f"{name}: {avg:.2f}")
    else:
        print(f"{name}: No grades available")

# 2. Find students who passed (average >= 50)
passed_students = list(filter(lambda s: calculate_average(s) is not None and calculate_average(s) >= 50, students))
print("\n--- Students Who Passed ---")
for s in passed_students:
    avg = calculate_average(s)
    print(f"{s['name']}: {avg:.2f}")

# 3. Sort students by average grade (highest first)
sorted_students = sorted(
    [s for s in students if calculate_average(s) is not None],
    key=lambda s: calculate_average(s),
    reverse=True
)
print("\n--- Students Sorted by Average Grade ---")
for s in sorted_students:
    print(f"{s['name']}: {calculate_average(s):.2f}")

# 4. Increase each student's grades by 5 (max 100)
def increase_grade(grade):
    return min(grade + 5, 100)

print("\n--- Updated Grades ---")
for student in students:
    student["grades"] = list(map(lambda g: increase_grade(g), student["grades"]))
    print(f"{student['name']}: {student['grades']}")

# 5. Handle students with no grades
# Already handled in the average calculation above

# 6. Generate summary report
summary = [(student["name"], calculate_average(student)) for student in students if calculate_average(student) is not None]

highest_grade = max(
    [grade for student in students for grade in student["grades"]],
    default=None
)

highest_students = [student["name"] for student in students if highest_grade in student["grades"]]

print("\n--- Summary Report ---")
print(f"Highest grade in the class: {highest_grade}")
print(f"Student(s) with the highest grade: {', '.join(highest_students)}")
