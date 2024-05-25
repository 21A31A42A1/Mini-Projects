import random
class College:
    def __init__(self):
        self.courses = {"CSE":10,"ECE":10,"MECH":10}
        self.staff = []
        self.students = []
        pass
class Student(College):
    def __init__(self, name, course, college):
        self.name = name
        self.course = course
        self.id = random.randint(100,200)
        college.courses[c] -= 1
    def giveid(self):
        return self.id
class Faculty(College):
    def __init__(self, name, branch, des):
        self.name = name
        self.branch = branch
        self.des = des
        self.id = "PEC"+str(random.randint(1,20))
        
pec = College()
while True:
    print("----------Welcome to portal of PEC------------")
    print("1. New Admission")
    print("2. New Staff")
    print("3. Staff info")
    print("4. Student Info")
    print("5. Exit")
    choice = int(input("Choose any option: "))
    if choice == 5:
        print("Thank You...!")
        break
    elif choice == 1:
        name = input("Enter your name: ")
        print("Courses available are: ")
        for i in pec.courses:
            print(f"{i} - Available seats: {pec.courses[i]}")
        c = input("Enter the course: ")
        if pec.courses[c] == 0:
            print("No seats available in that course...Sorry")
        else:
            st = Student(name, c, pec)
            print(f"Name: {st.name}")
            print(f"Course: {st.course}")
            pec.students.append(st)
            x = Student.giveid(st)
            print(f"We confirm your admission. Your id is ->{x}<-. Store it for future reference")
    elif choice == 2:
        name = input("Name of the Faculty: ")
        des = input("Enter the designation: ")
        branch = input("Enter the Branch (CSE, ECE, MECH): ")
        st = Faculty(name, branch, des)
        pec.staff.append(st)
        print(f"{st.id} is your ID, Store it for futture references. Happy Teaching :)")
    elif choice == 3:
        print("The faculty details are")
        print("id     Name    Designation    Branch")
        for i in pec.staff:
            print(f"{i.id} {i.name}   {i.des}   {i.branch}")
    elif choice == 4:
        print("The student details are: ")
        print("id   Name    Course")
        for i in pec.students:
            print(f"{i.id}   {i.name}   {i.course}")
    else:
        print("Enter Valid Choice...")