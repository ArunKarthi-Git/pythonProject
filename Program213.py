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
            big = big if L[i] > big else L[i]
            big2 = big2 if L[i]>big and big2 > big else L[i]
        for i in range(len(L)):
            small= small if L[i] < small else L[i]
            small2 = small2 if L[i] < small and small<small2 else L[i]
        print("The biggest of 2nd no. is",big2)
        print("The smallest of 2nd no. is", small2)


    a=int(input("Enter the len no."))
    read(a)
    display()
