classdict = {}
adding = input("")
while adding != "No":
    studentname = input("Please enter the name of the student: ").capitalize()
    adding = input("Would you like to add another student to your class (yes/no): ").capitalize()
    classdict[studentname] = []
print(classdict)

adding = input("")
while adding != "No":
    student = input("Which student would you like to add a grade for?: ").capitalize()
    grade = int(input("Enter their grade: "))
    classdict[student].append(grade)
    adding = input("Would you like to add another grade (yes/no): ").capitalize()
print(classdict)

adding = input("")
while adding != "No":
    student = input("Which student would you like to calculate the overall grade for?: ").capitalize()
    for student, value in classdict.items():
        overall = (sum(value)/len(value))
        if overall >= 89.5:
            print(overall, "A")
        elif (overall <= 89.5 and overall >= 79.5):
            print(overall, "B")
        elif (overall <= 79.5 and overall >= 69.5):
            print(overall, "C")
        elif (overall <= 69.5 and overall >= 59.5):
            print(overall, "D")
        else:
            print(overall, "F")
    adding = input("Would you like to calculate another student's grade (yes/no): ").capitalize()
print(classdict)
