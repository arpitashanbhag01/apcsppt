classdict = {}
adding = input("")
while adding != "No":
    while True:
        studentname = input("Please enter the name of the student: ").strip().capitalize()
        if studentname not in classdict:
            classdict[studentname] = []
            break
        else:
            print(studentname, "is already in the class list. Please list a different student.")
    while True:
        adding = input("Would you like to add another student to your class (yes/no): ").strip().capitalize()
        if adding in ("Yes", "No"):
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
print(classdict)

adding = input("")
while adding != "No":
    while True:
        student = input("Which student would you like to add a test score for?: ").strip().capitalize()
        if student in classdict.keys():
            break
        else:
            print("This student is not part of your list.")
            #would you like to add them to your list
    while True:
        grade = (input("Enter their test score: "))
        if grade.isdigit():
            classdict[student].append(grade)
            break
        else:
            print("Please enter a valid test score.")
    adding = input("Would you like to add another test score (yes/no): ").strip().capitalize()
print(classdict)

adding = input("")
while adding != "No":
    while True:
        student = input("Which student would you like to calculate the overall grade for?: ").strip().capitalize()
        if student in classdict.keys():
            break
        else:
            print("This student is not part of your list.")
    for student, value in classdict.items():
        #if len(value) = 0 ignore
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
    adding = input("Would you like to calculate another student's grade (yes/no): ").strip().capitalize()
print(classdict)
