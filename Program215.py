if __name__=='__main__':
    def Read(L,s):
        for j in range(s):
            L.append(input("Enter a No."))

    def Display(L):
        i=len(L)
        for j in range(i):
            print(L[j])

    s=int(input("Enter List Size"))
    L=[]
    Read(L,s)
    Display(L)


