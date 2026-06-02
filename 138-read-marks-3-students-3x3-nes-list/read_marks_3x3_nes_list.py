# WAP to read marks for 3 students and 3 subjects (3x3)
stud = []
print("Enter Marks of Students 9 times ")

for i in range(3):
    marks = []  # [] [] []

    for j in range(3):
        values = int(input("Enter marks : "))
        marks.append(values)
    stud.append(marks)

print("\nstud")
