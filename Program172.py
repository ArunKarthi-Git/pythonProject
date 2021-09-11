class Student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def insert(self):
        L = ["\nName:",self.name,"\nAge:", self.age,"\nAddress:", self.address[0],"\n ",self.address[1],"\n ",self.address[2]]
        f.writelines(L)

L=[]
i=0
name=input("Enter the name")
L.append(name)
f = open("/home/karthi/Document/Student1.txt", "w")
i=0
while L[i]!='$':
    age = input("Enter the Age:")
    address = []
    address.append(input("Enter the Street"))
    address.append(input("Enter the City"))
    address.append(input("Enter the Pin"))
    s = Student(name, age, address)
    s.insert()
    i+=1
    name = input("Enter the Name:")
    L.append(name)
f.close()
