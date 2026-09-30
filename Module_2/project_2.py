# Student Grade Calculator

print("=== Student Grade Calculator ===")
name = input("Enter student name: ")
subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    subject = input("Enter subject name: ")
    marks = float(input("Enter marks: "))
    total += marks

maximum = subjects * 100
percentage = (total / maximum) * 100

# Calculate grade
if percentage >= 90:
    grade = "A+"
    remark = "Outstanding"
elif percentage >= 80:
    grade = "A"
    remark = "Excellent"
elif percentage >= 70:
    grade = "B"
    remark = "Very Good"
elif percentage >= 60:
    grade = "C"
    remark = "Good"
elif percentage >= 50:
    grade = "D"
    remark = "Satisfactory"
elif percentage >= 40:
    grade = "E"
    remark = "Pass"
else:
    grade = "F"
    remark = "Needs Improvement"

# Display result
print("\n===== GRADE REPORT =====")
print("Student:", name)
print("Total Marks:", total, "/", maximum)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Remark:", remark)