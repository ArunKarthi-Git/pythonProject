import sys


class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def writeIntoFile(self):

        #content="name:"+self.name+"age:",self.age,"address:",self.address[0],self.address[1],self.address[2]"
        #f.write('"name:"+self.name+"age:" self.age "address:" self.address[0] self.address[1] self.address[2]"')
        #L = ["Name:",self.name,"\nAge:", self.age,"\nAddress:", self.address[0],"\n ",self.address[1],"\n ",self.address[2]]
        print(self.name,self.age,self.salary)
        L=[self.name," " ,self.age," ",self.salary+"\n"]
        f.writelines(L)
        #f.write(content)


flag=True
i=0
f = open(sys.argv[1], "w")
L=[]
while True:
    if flag!="N":
        name = input("Enter the Name:")
        age = input("Enter the Age:")
        salary = input("Enter the Salary")
        e=Employee(name,age,salary)
        e.writeIntoFile()
        i+=1
        flag=input("Do u want to continue !.. Press Y or  N")
    else:
        sys.exit()
f.close()