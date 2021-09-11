class Student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def writeIntoFile(self):
        f = open("/home/karthi/Document/Student1.txt", "w")
        #content="name:"+self.name+"age:",self.age,"address:",self.address[0],self.address[1],self.address[2]"
        #f.write('"name:"+self.name+"age:" self.age "address:" self.address[0] self.address[1] self.address[2]"')
        L = ["Name:",self.name,"\nAge:", self.age,"\nAddress:", self.address[0],"\n ",self.address[1],"\n ",self.address[2]]
        f.writelines(L)
        #f.write(content)
        f.close()

name=input("Enter the Name:")
age=input("Enter the Age:")
address=[]
address.append(input("Enter the Street"))
address.append(input("Enter the City"))
address.append(input("Enter the Pin"))
s=Student(name,age,address)
s.writeIntoFile()

