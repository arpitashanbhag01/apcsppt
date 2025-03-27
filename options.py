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
    grade = input("Enter their grade: ")
    classdict[student].append(grade)
    adding = input("Would you like to add another grade (yes/no): ").capitalize()
print(classdict)
