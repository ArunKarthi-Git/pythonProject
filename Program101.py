if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    L1=[]
    j=0
    L1.append(input("Enter the character"))
    while L1[j] !='$':
        j+=1
        L1.append(input("Enter the character"))
    L1[j]='.'

    print(L)
    print(L1)
    k=0
    count=0
    while L[k]!='.':
        M=0
        N=k
        while L1[M]==L[N] and L1[M]!='.':
            M+=1
            N+=1
            if L1[M]=='.':
                count+=1
        k+=1
    print("pattern Exit",count," times")