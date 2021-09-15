if __name__=='__main__':
    L=[]
    def read(a):
        for i in range(a):
           L.append(int(input("Enter the No.")))

    def display():
        big=0
        for i in range(len(L)):
            if L[i] > big:
                big=L[i]

        print("The biggest no. is",big)


    a=int(input("Enter the len no."))
    read(a)
    display()
