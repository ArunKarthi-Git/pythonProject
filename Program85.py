if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] != '$':
        i+=1
        L.append(input("Enter the character"))
    L.append('.')
    L1=[]
    i=0
    while L[i] !='.':
        if L[i]!=',':
            L1.append(L[i])
        i+=1
    L1.append('.')
    k=0
    while L[k]!='.':
        print(L1[k])
        k+=1


