class ReadChar:
    def __init__(self,ch):
        self.ch=ch

    def write(self,ch):
        f.write(self.ch)
        f.write("\n")



f = open("/home/karthi/Document/file10.txt", "w")
char=""
readchar=ReadChar(char)
readchar.ch=input("Enter the char")
ch1=readchar.ch
while ch1 !='$':
    readchar.write(ch1)
    readchar.ch = input("Enter the char")
    ch1=readchar.ch

f.close()
