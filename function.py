classdict = {}
def addstudent(studentname):
    while True:
        if studentname not in classdict:
            classdict[studentname] = []
            break
        else:
            print(studentname, "is already in the class list. Please list a different student.")

def calculategrade(student):
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

numstudent = int(input("How many students would you like to add to your class?: "))
for i in range (numstudent):
    studentname = input("Please enter the name of the student: ").strip().capitalize()
    addstudent(studentname)
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
        grade = int((input("Enter their test score: ")))
        #fix isdigit
        if grade.isdigit():
            classdict[student].append(grade)
            break
        else:
            print("Please enter a valid test score.")
    adding = input("Would you like to add another test score (yes/no): ").strip().capitalize()
whostudent = input("Who do you want to calculate a grade for?: ")
calculategrade(whostudent)
print(classdict)
