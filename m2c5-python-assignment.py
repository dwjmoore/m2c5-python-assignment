#Exercise 1
student = {
    "name": "Bob",
    "age": 18,
    "major": "Computer Science",
    "year": 2026,
    "classes": "Python",
}

print("Exercise 1")
print(student)
print()

#Exercise 2
print("Exercise 2")
print(student.get("name"))
print()

#Exercise 3
student.pop("year")
print("Exercise 3")
print(student)
print()

#Exercise 4
student["gpa"] = 3.9
print("Exercise 4")
print(student)
print()


#Exercise 5
student["gpa"] = 4.0
print("Exercise 5")
print(student)
print()

#Exercise 6

college_students = [
    {"name" : "Xander", "age" : 18, "major" : "Computer Science", "year" : 2026, "classes": "Python"},
    {"name" : "Henry", "age" : 19, "major" : "Math", "year" : 2025, "classes" : "Calculus"},
    {"name" : "Jill", "age" : 20, "major" : "History", "year" : 2024, "classes" : "American History"},
    {"name" : "Abe", "age" : 21, "major" : "Business", "year" : 2023, "classes" : "Finance"},
    {"name" : "Kellie", "age" : 22, "major" : "Music", "year" : 2022, "classes" : "Composing"}
]

print("Exercise 6")
print(college_students)
print()

#Exercise 7
def myFunc(x):
    return x["name"]

college_students.sort(key=myFunc)
print("Exercise 7")
print(college_students)
print()