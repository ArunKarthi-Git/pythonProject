import sys
# python Program177.py /home/karthi/Document/file10.txt
class program177:
    def __init__(self):
        self.geek = "GeekforGeeks"

    def display(self, line):
        print(line)


print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))
print(sys.argv[1])
f = open(sys.argv[1], "r")
myline = f.readline()

prg = program177()

while myline:
    prg.display(myline)
    myline = f.readline()
f.close()

