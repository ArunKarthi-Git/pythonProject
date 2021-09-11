class Student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def display(self):
        f = open("/home/karthi/Document/Student1.txt", "r")
        print(f.read())
        f.close()


s=Student("siva","23","Thuraiyur")
s.display()