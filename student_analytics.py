from collections import defaultdict
from typing import Dict, List


def create_student(name: str, roll: str, **marks) -> dict:
    """Create a student record."""

    if not name or not roll:
        raise ValueError("Name and roll required")

    if not marks:
        raise ValueError("At least one subject mark required")

    return {
        "name": name,
        "roll": roll,
        "marks": marks,
        "attendance": 0.0
    }


def calculate_gpa(*marks: float, scale: float = 10.0) -> float:
    """Calculate GPA."""

    if not marks:
        return 0

    avg = sum(marks) / len(marks)
    gpa = (avg / 100) * scale

    return round(gpa, 2)


def get_top_performers(students: List[Dict], n: int = 5, subject: str = None) -> List[Dict]:

    if not students:
        return []

    if subject:
        sorted_students = sorted(
            students,
            key=lambda x: x["marks"].get(subject, 0),
            reverse=True
        )
    else:
        sorted_students = sorted(
            students,
            key=lambda x: sum(x["marks"].values()) / len(x["marks"]),
            reverse=True
        )

    return sorted_students[:n]


def generate_report(student: Dict, **options) -> str:

    include_grade = options.get("include_grade", True)

    marks = student["marks"]
    avg = sum(marks.values()) / len(marks)

    report = f"Student: {student['name']} ({student['roll']})\n"
    report += f"Average: {avg}\n"

    if include_grade:
        if avg >= 90:
            grade = "A"
        elif avg >= 75:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        else:
            grade = "D"

        report += f"Grade: {grade}\n"

    return report


def classify_students(students: List[Dict]) -> Dict:

    result = defaultdict(list)

    for s in students:
        avg = sum(s["marks"].values()) / len(s["marks"])

        if avg >= 90:
            result["A"].append(s)
        elif avg >= 75:
            result["B"].append(s)
        elif avg >= 60:
            result["C"].append(s)
        else:
            result["D"].append(s)

    return dict(result)