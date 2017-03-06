def employee_skills(surname, name, experience, position):
    experience = int(experience)
    if experience < 3:
        exp_score = "junior"
    if 3 <= experience < 7:
        exp_score = "middle"
    if experience >= 7:
        exp_score = "senior"
    print(name + " " + surname + " is " + exp_score +" "+ position)


file = open("workers2.txt")
#employees = {}
for line in file:
    emp_list = dict.fromkeys(["surname", "name", "position", "experience"])
    line = line.rstrip().split()
    emp_list["surname"] = line[0]
    emp_list["name"] = line[1]
    emp_list["position"] = line[2]
    emp_list["experience"] = line[3]
    employee_skills(**emp_list)
file.close()
