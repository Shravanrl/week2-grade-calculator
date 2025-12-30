
def calculate_grade(avg):
    if avg >= 90:
        return "A", "Excellent!"
    elif avg >= 80:
        return "B", "Very Good!"
    elif avg >= 70:
        return "C", "Good"
    elif avg >= 60:
        return "D", "Needs Improvement"
    else:
        return "F", "Failed - Please seek help"

def get_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")

students = []

try:
    n = int(input("Number of students: "))
except ValueError:
    print("Invalid number.")
    exit()

for i in range(n):
    print(f"=== STUDENT {i+1} ===")
    name = input("Name: ")
    math = get_mark("Math")
    science = get_mark("Science")
    english = get_mark("English")

    avg = round((math + science + english) / 3, 1)
    grade, comment = calculate_grade(avg)

    students.append({
        "name": name,
        "avg": avg,
        "grade": grade,
        "comment": comment
    })

print("\nRESULTS SUMMARY")
print("Name\t\tAvg\tGrade\tComment")
for s in students:
    print(f"{s['name']}\t{s['avg']}\t{s['grade']}\t{s['comment']}")

avgs = [s["avg"] for s in students]
print("\nCLASS STATISTICS")
print("Total Students:", len(students))
print("Class Average:", round(sum(avgs)/len(avgs), 1))
print("Highest Average:", max(avgs))
print("Lowest Average:", min(avgs))
