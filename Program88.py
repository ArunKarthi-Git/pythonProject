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
    merge=[]
    k=0
    while L[k] !='.':
        merge.append(L[k])
        k+=1
    l=0
    while L1[l] !='.':
        merge.append(L1[l])
        l+=1
    merge.append('.')
    m=0
    while merge[m] !='.':
        merge[m]
        m+=1
    print(L)
    print(L1)
    print(merge)

