import sys

#python Program176.py /home/karthi/Document/file10.txt siva 23 Thuraiyur

class program176:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        L = self.name + "\n" + self.age + "\n" + self.address
        f.writelines(L)

print('Number of arguments:', len(sys.argv))
print('Argument List:', str(sys.argv))

print(sys.argv[1])
f = open(sys.argv[1], "w")
name = sys.argv[2]
age = sys.argv[3]
address = sys.argv[4]
prg = program176(name, age, address)
prg.display()
f.close()




