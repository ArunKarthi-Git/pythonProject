import sys

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self):

        #content="name:"+self.name+"age:",self.age,"address:",self.address[0],self.address[1],self.address[2]"
        #f.write('"name:"+self.name+"age:" self.age "address:" self.address[0] self.address[1] self.address[2]"')
        #L = ["Name:",self.name,"\nAge:", self.age,"\nAddress:", self.address[0],"\n ",self.address[1],"\n ",self.address[2]]
        hra=float(self.salary)*0.01
        da=float(self.salary)*0.02
        print_name=self.name
        print_age=self.age
        print_salary=self.salary
        print('{0} {1} {2} '.format(print_name,hra,da))


flag=True
i=0
f = open(sys.argv[1], "r")
L=[]
for line in f:
    s=line.split(" ")
    name=s[0]
    age=s[1]
    salary=s[2]
    e=Employee(name,age,salary)
    e.display()
f.close()