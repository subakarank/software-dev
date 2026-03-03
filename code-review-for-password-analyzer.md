# 🔍 Password Analyzer – Code Review Checklist

Use this checklist to review your partner’s project.
Focus on **functionality** and **code quality**.

---

# 1️⃣ Functional Review

## ✅ Output Structure
- Returns a dictionary
- Contains:
  - `"summary"` → `total_passwords`, `duplicates`
  - `"results"` → list of:
    - `password`
    - `strength`
    - `score`
    - `issues`

---

## ✅ Mandatory Functions (Must Exist & Be Used)

- `analyze_password(password)`
- `find_duplicates(password_list)`
- `max_repeating_streak(password)`  *(must use two-pointer logic)*
- `calculate_score(results_dict)`
- `generate_report(passwords)`

---

## ✅ Rule Check Functions

- `check_length(pwd)` → length ≥ 10
- `has_upper(pwd)`
- `has_lower(pwd)`
- `has_digit(pwd)`
- `has_special(pwd)`

Each rule should be implemented as a separate function.

---

## ✅ Repeated Character Logic

- Uses **two-pointer approach**
  - `i` → start of streak
  - `j` → moves forward while characters match
- Flags issue if **more than 3 repeated characters in a row**

Examples:
- `"aaaa"`
- `"1111"`
- `"!!!!"`

---

## ✅ Common Password Detection

- Uses a `set`
- Includes common passwords like:
  - `"password"`
  - `"123456"`
  - `"qwerty"`
  - `"admin"`
- Applies penalty correctly

---

## ✅ Duplicate Detection

- Uses a `set`
- Correctly counts repeated passwords
- Summary shows correct duplicate count

---

## ✅ Scoring & Strength Classification

Scoring Rules:

- +20 → Length ≥ 10
- +15 → Uppercase
- +15 → Lowercase
- +15 → Digit
- +15 → Special character
- −20 → Repeated characters
- −30 → Common password

Score must be between **0–100**

Strength Mapping:

- 80–100 → Strong
- 50–79 → Medium
- <50 → Weak

---

# 2️⃣ Code Quality Review

## ✅ Structure

- No classes
- No UI
- `generate_report()` controls overall flow
- Each function does **one clear job**

---

## ✅ Clean Code

- Clear variable and function names
- No duplicated logic
- No unnecessary `print()` inside core functions
- No global variables affecting logic

---

## ✅ Correct Data Structures

- `set` → common passwords, duplicates
- `list` → issues, results
- `dict` → final report structure

---

## ✅ Edge Case Handling

- Works with empty list
- Works with short passwords
- No crashes on unusual input

---

## ✅ Readability

- Proper indentation
- Logical order of functions
- Two-pointer logic easy to understand

---

# 📝 Reviewer Feedback

## ✔ Strengths
- 
- 
- 

## ⚠ Improvements
- 
- 
- 
