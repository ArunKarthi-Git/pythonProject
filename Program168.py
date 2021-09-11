import pdb


class Bio:
    def __init__(self,name,age,course,address):
        self.name=name
        self.age=age
        self.course=course
        self.address=address

    def print(self):
        print(self.name,"\n",self.age,"\n",self.course,"\n",self.address[0],"\n",self.address[1],"\n",self.address[2])

name=input("Enter a name")
age=int(input("Enter a age"))
course=input("Enter a course")
L=[]
L.append(input("Enter a street"))
L.append(input("Enter a city"))
L.append(input("Enter a pin"))

T=(L)
B1=Bio(name,age,course,T)
B1.print()