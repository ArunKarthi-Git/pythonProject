if __name__=='__main__':
    L=[]
    def read(a):
        for i in range(a):
           L.append(int(input("Enter the No.")))

    def display():
        for i in range(len(L)):
            print(L[i])

    a=int(input("Enter the len no."))
    read(a)
    display()
