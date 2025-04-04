classdict = {}
def addstudent(studentname):
    while True:
        if studentname not in classdict:
            classdict[studentname] = []
            break
        else:
            print(studentname + " is already in the class list.")
            studentname = input("Please list a different student: ").strip().capitalize()

def calculategrade(student):
    gradelist = classdict.get(student)
    print(gradelist)
    grade = 0
    for i in gradelist:
        grade += i
        overall = (grade/len(gradelist))
        if overall >= 89.5:
            print(student, overall, "A")
        elif (overall <= 89.5 and overall >= 79.5):
            print(student, overall, "B")
        elif (overall <= 79.5 and overall >= 69.5):
            print(student, overall, "C")
        elif (overall <= 69.5 and overall >= 59.5):
            print(student, overall, "D")
        else:
            print(student, overall, "F")

while True:
  try:
    numstudent = int(input("How many students would you like to add to your class?: "))
    break
  except ValueError:
    print("Invalid input. Please enter an integer.")

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
            print("This student is not part of your class.")
            #would you like to add them to your list
    while True:
      try:
        grade = int((input("Enter their test score: ")))
        break
      except ValueError:
        print("Please enter a valid test score.")
    
    classdict[student].append(grade)
    adding = input("Would you like to add another test score (yes/no): ").strip().capitalize()

gradelist = classdict.get("Arpita")
print(gradelist)  

whostudent = input("Who do you want to calculate a grade for?: ")
calculategrade(whostudent)
print(classdict)
