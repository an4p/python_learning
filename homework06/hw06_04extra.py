departments = {'Developers': 10, 'QA': 5, 'Admins': 2, 'DevOps': 2,
               'Security': 1, 'BA': 2, 'HR': 1, 'OfficeManager': 1,
               'HelpDesk': 1, 'Support': 2}
print("The current list of the departments: ")
for dep in departments:
    print(dep)
while True:
    print("\n* For exit type 'Exit'. \n* To know general number of employees type 'All'.",
          "\n* To modify the Department type 'Modify'.",
          "\n* To create new Department type 'Create'")
    userInput = input("Enter the Department name:\n")#.capitalize()
    if userInput == 'Exit':
        break
    if userInput in departments:
        print(userInput, departments[userInput])
        continue
    if userInput == 'All':
        counter = 0
        for d in departments:
            counter += departments[d]
        print("General amount of employees: " + str(counter))
        continue
    if userInput == "Modify":
        depName = input("What is the department you want to change the employees number?\n")#.capitalize()
        if depName in departments:
            num = input("Enter a new number of employees in this department: \n")
            if num.isnumeric():
                departments[depName] = int(num)
                print("Information updated:")
                print(depName, departments[depName])
            else:
                print("Something went wrong")
    if userInput == "Create":
        newDep = input("What is the name of a new Department?\n")
        departments.setdefault(newDep, 0)
        num = input("Enter a new number of employees in this department: \n")
        if num.isnumeric():
            departments[newDep] = int(num)
            print("Information updated:")
            print(newDep, departments[newDep])
        else:
            print("This is not a number. The default value has been set to 0")
            print("Information updated:")
            print(newDep, departments[newDep])
    else:
        print("There is no such department")
