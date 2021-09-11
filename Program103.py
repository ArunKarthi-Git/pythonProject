if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the Character"))
    while L[i]!='$':
        i+=1
        L.append(input("Enter the Character"))
    L[i]='.'

    L1=[]
    j=0
    L1.append(input("Enter the Character"))
    while L1[j]!='$':
        j+=1
        L1.append(input("Enter the Character"))
    L1[j]='.'

    L2=[]
    k=0
    L2.append(input("Enter the Character"))
    while L2[k]!='$':
        k+=1
        L2.append(input("Enter the Character"))
    L2[k]='.'

    print(L)
    print(L1)
    print(L2)
    m=0
    L3=[]
    while L[m] !='.':
        n=0
        o=m
        while L1[n]==L[o] and L1[n]!='.':
            n+=1
            o+=1
        if L1[n] =='.':
            j=0
            while L2[j] !='.':
                L3.append(L2[j])
                j+=1
            m=o
        else:
            L3.append(L[m])
            m+=1
    q = 0
    L3.append('.')
    while L3[q] != '.':
        print(L3[q])
        q+=1



