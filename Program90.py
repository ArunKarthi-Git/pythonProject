if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the Character"))
    L.append('.')
    j=0
    L1=[]
    while L[j] !='.':
        if(L[j]=='='):
            L1.append(':')
        if (L[j] == "\n"):
            L1.append(';')
        L1.append(L[j])
        j+=1

    L1.append('.')
    k=0
    L2=''
    while L1[k] !='.':
        L2=L2+L1[k]
        k+=1
    print(L2)
