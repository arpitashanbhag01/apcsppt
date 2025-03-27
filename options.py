classdict = {}
adding = input("")
while adding != "No":
    #deal with repeating names
    studentname = input("Please enter the name of the student: ").strip().capitalize()
    while True:
        adding = input("Would you like to add another student to your class (yes/no): ").strip().capitalize()
        if adding in ("Yes", "No"):
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
    classdict[studentname] = []
print(classdict)

adding = input("")
while adding != "No":
    while True:
        student = input("Which student would you like to add a grade for?: ").strip().capitalize()
        if student in classdict.keys():
            break
        else:
            print("This student is not part of your list.")
            #would you like to add them to your list
    #check if their input is an integer .isdigit()
    grade = int(input("Enter their grade: "))
    classdict[student].append(grade)
    adding = input("Would you like to add another grade (yes/no): ").strip().capitalize()
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
