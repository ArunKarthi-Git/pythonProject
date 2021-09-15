import sys
import os

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self,n):
        i=0
        for i in range(0, len(L)):
            if i == n:
                print(L[i].name, L[i].age, L[i].salary)



f = open(sys.argv[1], "r")
string_list = f.readlines()
f.close()
L=[]
search_name=input("Enter the name to search")
salary_update=int(input("Enter the Salary"))
for line in string_list:
    s=line.split(" ")
    print(s)
    name=s[0]
    age=s[1]
    salary=s[2]
    print(name,search_name)
    if name==search_name:
        print(salary,salary_update)
        pos=line.index(salary)
        print(line.index(salary))
        salary=salary_update
        e = Employee(name, age, salary)
        #f.seek(pos)
        s[0]=name
        s[1]=age
        s[2]=salary
        L.append(s)
    else:
        L.append(s)

f1 = open(sys.argv[1], "w")
f1.write(str(L))
f1.close()