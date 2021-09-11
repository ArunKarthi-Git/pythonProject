class ReadChar:
    def __init__(self,ch):
        self.ch=ch

    def display(self,ch):
        print(self.ch)

file=open("/home/karthi/Document/file10.txt", "r")
fileLine=file.read()
s=ReadChar(fileLine)
while fileLine:
    s.display(fileLine)
    fileLine = file.read()

file.close()

