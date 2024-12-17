grades = {
    "Alice": 78,
    "Bob": 42,
    "Charlie": 65,
    "Diana": 49,
    "Eve": 90
}

def categorize(grades_list):
    student_categories = {}
    for student, grade in grades_list.items():
        if grade >= 50:
            student_categories[student] = "Pass"
        else:
            student_categories[student] = "Fail"

    print("Student Categories:")
    for student, category in student_categories.items():
        print(f"{student}: {category}")

if __name__ == "__main__":
    categorize(grades)
