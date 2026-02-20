# Input
name = input("Enter student name: ")
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

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
print("\n--- Result ---")
print("Name:", name)
print("Total:", total, "/300")
print("Percentage:", round(percentage, 1), "%")
print("Grade:", grade)