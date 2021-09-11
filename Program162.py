class Bio:
    def __init__(self,name,age,address,course):
        self.name=name
        self.age=age
        self.address=address
        self.course=course

    def printDetails(self):
        print(self.name,self.age,self.address,self.course)

student1=Bio("karthi",32,"Thuraiyur","MCA")
student2=Bio("shibu","23","Trichy","B.E")
student1.printDetails()
student2.printDetails()