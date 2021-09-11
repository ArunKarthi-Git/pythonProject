class student:
    def __init__(self):
        self.geek = "GeekforGeeks"

    def display(self,myline):
        print(myline)


myfile = open("/home/karthi/Document/Student1.txt", "r")
myline = myfile.readline()
s=student()
while myline:
    s.display(myline)
    myline = myfile.readline()

myfile.close()