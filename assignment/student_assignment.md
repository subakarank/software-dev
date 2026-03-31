# Assignment: Student Management System (Python)

## Objective
Practice working with multiple Python files, functions, lists, and dictionaries by building a simple student management system.

---

## Requirements

You need to create **three Python files**:

1. `main.py`  
2. `student.py`  
3. `student_data.py`  

---

## 1. student_data.py

- Create a variable called `student_data`
- It should be a **list of dictionaries**
- Each dictionary represents a student with the following fields:
  - `name` (string)
  - `age` (integer)
  - `class` (string)
  - `subjects` (list of strings)

### Example:
```python
student_data = [
    {
        "name": "John",
        "age": 15,
        "class": "10th",
        "subjects": ["Math", "Science"]
    },
    {
        "name": "Emma",
        "age": 14,
        "class": "9th",
        "subjects": ["English", "History"]
    }
]
```

---

## 2. student.py

Create the following two functions:

### add_student
```python
def add_student(students, student):
    students.append(student)
```

### delete_student
```python
def delete_student(students):
    if students:
        students.pop()
```

---

## 3. main.py

### Step 1: Import modules
```python
from student import add_student, delete_student
from student_data import student_data
```

### Step 2: Create an empty list
```python
students = []
```

### Step 3: Perform operations
```python
# Add the first student
add_student(students, student_data[0])
print("After adding student:")
print(students)

# Delete the last student
delete_student(students)
print("\nAfter deleting student:")
print(students)

# Add again
add_student(students, student_data[0])
print("\nAfter adding again:")
print(students)
```

---

## Bonus (Optional)
- Add validation messages
- Handle empty list cases
