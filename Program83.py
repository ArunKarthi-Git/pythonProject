if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    print(L)
    L1=[]
    j=0
    i=0
    while L[i] !='.':
        print(L[i])
        if ord(L[i])>=65 and ord(L[i])<=90:
            L1.append(chr(ord(L[i])+32))
        else:
            L1.append(L[i])
        i+=1
    print(L1)
    L1.append('.')
    j=0
    while L1[j] !='.':
        print(L1[j])
        j+=1
