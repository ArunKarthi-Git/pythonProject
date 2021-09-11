import sys

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


flag=True
f = open(sys.argv[1], "r")
L=[]
for line in f:
    s=line.split(" ")
    name=s[0]
    age=s[1]
    salary=s[2]
    e=Employee(name,age,salary)
    L.append(e)
n=int(input("Enter the nth record to display"))
if n>len(L):
    print(n,"is greater then the list")
    f.close()
    sys.exit(1)
e.display(n)

f.close()