if __name__=='__main__':
    L=[]
    def read(a):
        for i in range(a):
           L.append(int(input("Enter the No.")))

    def display():
        big=0
        big2=0
        small=L[0]
        small2=L[0]
        for i in range(len(L)):
            big = L[i] if L[i] > big else big
        print(big)
        for i in range(len(L)):
            big2 = L[i] if L[i]>big2 and L[i] != big else big2
        print(big2)
        for i in range(len(L)):
            small= L[i] if L[i] < small else small
        print(small)
        for i in range(len(L)):
            small2 = L[i] if L[i] < small2 and L[i]!=small else small2
        print(small2)
        print("The biggest of 2nd no. is",big2)
        print("The smallest of 2nd no. is", small2)


    a=int(input("Enter the len no."))
    read(a)
    display()
