if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the Character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the Character"))
    L[i]='.'
    L1=[]
    j=0
    L1.append(input("Enter the Character"))
    while L1[j] !='$':
        j+=1
        L1.append(input("Enter the Character"))
    L1[j]='.'

    L2=[]
    K=0
    O=0
    print(L)
    print(L1)
    while L[K]!='.':
        M=0
        N=K
        while L1[M]==L[N] and L1[M]!='.':
            M+=1
            N+=1
        if L1[M] =='.':
            K=N
        else:
            O+=1
        L2.append(L[N])
        K+=1
    L2.append('.')
    P=0
    while L2[P] !='.':
        print(L2[P])
        P+=1
    print(L2)

