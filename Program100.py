if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] != '$':
        i+=1
        L.append(input("Enter the Character"))
    L[i]='.'

    L1=[]
    j=0
    L1.append(input("Enter the pattern character"))
    while L1[j] != '$':
        j+=1
        L1.append(input("Enter the pattern character"))
    L1[j]='.'

    print(L)
    print(L1)
    k=0
    while L[k] !='.':
        M=0
        N=k
        print(M,N)
        while L1[M] == L[N] and L1[M]!='.':
            print(L1[M], L[N])
            M+=1
            N+=1
            if L1[M]=='.':
                print("Pattern Exit")
                exit()
        k+=1
    print("Pattern Not Exit")
