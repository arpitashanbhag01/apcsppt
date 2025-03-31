classdict = {}
def addstudent(studentname):
    while True:
        if studentname not in classdict:
            classdict[studentname] = []
            break
        else:
            print(studentname, "is already in the class list. Please list a different student.")

numstudent = int(input("How many students would you like to add to your class?: "))
for i in range (numstudent):
    studentname = input("Please enter the name of the student: ").strip().capitalize()
    addstudent(studentname)
print(classdict)
