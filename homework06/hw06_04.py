departments = {'Developers': 10, 'QA': 5, 'Admins': 2, 'DevOps': 2,
               'Security': 1, 'BA': 2, 'HR': 1, 'OfficeManager': 1,
               'HelpDesk': 1, 'Support': 2}
for dep in departments:
    print(dep)
while True:
    print("For exit type 'Exit'")
    userInput = input("Enter the Department name:\n").capitalize()
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
    else:
        print("There is no such department")