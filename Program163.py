class Bio:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printDetails(self):
        print(self.name,self.age)

name=input("Enter a name")
age=input("Enter a age")
student=Bio(name,age)
student.printDetails()