from student_analytics import *

students = [
    create_student("Amit", "R001", math=85, python=92, ml=78),
    create_student("Priya", "R002", math=95, python=88, ml=91)
]

assert calculate_gpa(85,92,78) > 0

top = get_top_performers(students,1,"python")
assert top[0]["name"] == "Amit"

report = generate_report(students[0])
assert "Student" in report

groups = classify_students(students)
assert isinstance(groups, dict)

print("All tests passed")