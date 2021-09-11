class Student:
    def __init__(self,name,age,address,course):
        self.name=name
        self.age=age
        self.address=address
        self.course=course

    def display(self):
        print("name:",self.name,"age:",self.age,"address:",self.address[0],self.address[1],self.address[2],"Course:",self.course)

i=3
s=[]
for i1 in range(i):
    name=input("Enter a name")
    age=input("Enter a age")
    address=[]
    address.append(input("Enter a street"))
    address.append(input("Enter a city"))
    address.append(input("Enter a pin"))
    course=input("Enter the course")
    s.append(Student(name,age,address,course))

j=3
for j1 in range(j):
    s[j1].display()