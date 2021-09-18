if __name__=='__main__':
    L=[]
    def read(a):
        for i in range(a):
           L.append(int(input("Enter the No.")))

    def compareAndSwap():
        pb1=1
        pb2=1
        ps1=1
        ps2=1
        for i in range(len(L)):
            pb1=i if L[i] > L[pb1] else pb1
        for i in range(len(L)):
            pb2= i if L[i]>L[pb2] and L[i] != L[pb1] else pb2
        for i in range(len(L)):
            ps1 = i if L[i] < L[ps1] else ps1
        for i in range(len(L)):
            ps2 = i if L[i] < L[ps2] and L[i] != L[ps1] else ps2
        t=L[pb2]
        L[pb2]=L[ps2]
        L[ps2]=t
    def display():
        for i in range(len(L)):
            print(L[i])


    a=int(input("Enter the len no."))
    read(a)
    compareAndSwap()
    display()
