# assignment_day_10_PM
assignment for week-2 day10
# Day 10 PM Assignment

## Part A — Student Performance Analytics Module

### Objective

Build a Python module that analyzes student performance using well-structured functions.
The module demonstrates the use of:

* Function definitions (`def`, `return`)
* Positional and keyword parameters
* `*args` and `**kwargs`
* Multiple return values
* Type hints (PEP 484)
* Google-style docstrings
* Default parameters
* Basic data analytics on student records

---

### Student Data Structure

Each student is stored as a dictionary with the following format:

```python
{
    "name": str,
    "roll": str,
    "marks": {
        "math": int,
        "python": int,
        "ml": int
    },
    "attendance": float
}
```

Example:

```python
create_student("Amit", "R001", math=85, python=92, ml=78)
```

---

### Functions Implemented

#### 1. `create_student()`

Creates a student record using flexible subject marks.

```python
create_student(name: str, roll: str, **marks) -> dict
```

Features:

* Accepts any number of subjects using `**kwargs`
* Validates required fields
* Returns a structured student dictionary

---

#### 2. `calculate_gpa()`

Calculates GPA from any number of marks.

```python
calculate_gpa(*marks: float, scale: float = 10.0) -> float
```

Features:

* Accepts unlimited marks using `*args`
* GPA scale configurable
* Handles empty input

Example:

```python
calculate_gpa(85, 92, 78)
```

Output:

```
8.5
```

---

#### 3. `get_top_performers()`

Returns the top performing students.

```python
get_top_performers(students: list[dict], n: int = 5, subject: str = None)
```

Features:

* Returns top **n** students
* Can rank by a specific subject
* Otherwise ranks by overall average

Example:

```python
get_top_performers(students, n=1, subject="python")
```

---

#### 4. `generate_report()`

Generates a formatted student report.

```python
generate_report(student: dict, **options) -> str
```

Options include:

* `include_grade`
* `include_rank`
* `verbose`

Example output:

```
Student: Amit (R001)
Average: 85
Grade: B
```

---

#### 5. `classify_students()`

Classifies students into grade groups.

```python
classify_students(students: list[dict]) -> dict
```

Grades:

| Grade | Average Marks |
| ----- | ------------- |
| A     | ≥ 90          |
| B     | ≥ 75          |
| C     | ≥ 60          |
| D     | < 60          |

Output structure:

```python
{
 "A": [...],
 "B": [...],
 "C": [...],
 "D": [...]
}
```

---

### Testing

All functions were tested using `test_analytics.py`.

Example:

```python
python test_analytics.py
```

Output:

```
All tests passed
```

Each function includes multiple test cases using `assert` statements to verify correct functionality.

---

### Key Concepts Demonstrated

* Flexible function parameters
* Python data structures
* Sorting and ranking
* Default parameters
* Clean modular code design
* Edge case handling

---

### Files Related to Part A

```
student_analytics.py
test_analytics.py
part_A.txt
```

These files implement the analytics module, tests, and sample results.

## Part B — Python Decorators

### Objective

This section demonstrates the implementation of **custom Python decorators**.
Decorators are functions that modify the behavior of other functions without changing their source code.

Decorators use **higher-order functions**, **closures**, and `*args` / `**kwargs` so they can work with any function signature.

---

### Decorators Implemented

#### 1️⃣ `@timer`

Measures the execution time of a function.

**Implementation Idea**

* Record start time using `time.time()`
* Execute the function
* Record end time
* Print execution duration

Example:

```python
@timer
def slow_function():
    time.sleep(1)
    return "Task Completed"
```

Example Output:

```
[TIMER] slow_function executed in 1.0002 seconds
Task Completed
```

---

#### 2️⃣ `@logger`

Logs function name, arguments, and return value.

Example:

```python
@logger
def add_numbers(a, b):
    return a + b
```

Example Output:

```
[LOGGER] Calling function: add_numbers
[LOGGER] Arguments: args=(5,3)
[LOGGER] Returned: 8
```

---

#### 3️⃣ `@retry(max_attempts=3)`

Retries a function if it raises an exception.

Useful when dealing with:

* network requests
* database queries
* unstable operations

Example:

```python
@retry(max_attempts=3)
def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"
```

Example Output:

```
[RETRY] Attempt 1 failed
[RETRY] Attempt 2 failed
Success
```

---

### Key Concepts Demonstrated

* Higher-order functions
* Closures
* Decorator pattern
* `functools.wraps`
* Flexible parameters (`*args`, `**kwargs`)
* Exception handling

---

### File Structure (Part B)

```
decorators.py
part_B.txt
```

* **decorators.py** → contains the implementations of `timer`, `logger`, and `retry`
* **part_B.txt** → contains example outputs and results

