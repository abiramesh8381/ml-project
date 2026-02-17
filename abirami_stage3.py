
# Stage 3: Student Grade Calculator

name = input("Enter student name: ")

mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

# Calculate total and percentage
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Grade logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print("\n" + name)
print(f"Total: {int(total)}/300")
print(f"Percentage: {percentage:.1f}%")
print("Grade:", grade)