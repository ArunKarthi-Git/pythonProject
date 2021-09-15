import sys
import os

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def writeIntoFile(self):
        # content="name:"+self.name+"age:",self.age,"address:",self.address[0],self.address[1],self.address[2]"
        # f.write('"name:"+self.name+"age:" self.age "address:" self.address[0] self.address[1] self.address[2]"')
        # L = ["Name:",self.name,"\nAge:", self.age,"\nAddress:", self.address[0],"\n ",self.address[1],"\n ",self.address[2]]
        print(self.name, self.age, self.salary)
        L = [self.name, " ", self.age, " ", self.salary ]
        f1.writelines(L)

    def editIntoFile(self):
        # content="name:"+self.name+"age:",self.age,"address:",self.address[0],self.address[1],self.address[2]"
        # f.write('"name:"+self.name+"age:" self.age "address:" self.address[0] self.address[1] self.address[2]"')
        # L = ["Name:",self.name,"\nAge:", self.age,"\nAddress:", self.address[0],"\n ",self.address[1],"\n ",self.address[2]]
        print(self.name, self.age, self.salary)
        L = [self.name, " ", self.age, " ", self.salary,"\n" ]
        f1.writelines(L)


f = open(sys.argv[1], "r")
string_list = f.readlines()
f.close()

search_name=input("Enter the name to search")
salary_update=input("Enter the Salary")
f1 = open(sys.argv[1], "w")
for line in string_list:
    s=line.split(" ")
    name=s[0]
    age=s[1]
    salary=s[2]
    print(name,"==",search_name)
    if name==search_name:
        pos=line.index(salary)
        salary=salary_update
        #f.seek(pos)
        s[0]=name
        s[1]=age
        s[2]=salary
        print(s[1],s[2])
        e = Employee(s[0],s[1],s[2])
        e.editIntoFile()
    else:
        s[0] = name
        s[1] = age
        s[2] = salary
        e = Employee(s[0],s[1],s[2])
        e.writeIntoFile()
f1.close()