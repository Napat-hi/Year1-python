def addstudent(name, score):
    if name not in students:
        students[name] = score
    else:
        print("Duplicate name!")

students = {}
while True:
    studentscore = input("Enter students name and score:").split()
    
    
    if studentscore[0] == "end" and studentscore[1] == "0":
        if not(students):
            print("List:\n> empty list!")
            break
        print("List:")
        
        dict(sorted(students.items(),key = lambda x:x[1] ))
        
        for name,score in students.items():
            print(f"{name}\t{score}")
        break
    if not 0 <= int(studentscore[1]) <= 100:
            print("Invalid score!")
            continue    
        
    
    addstudent(studentscore[0], studentscore[1])