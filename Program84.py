if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] != '$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    i=0
    L1=[]

    while L[i] !='.':
        
        if L[i]==',':
            L1.append(';')
        else:
            L1.append(L[i])
        i+=1
    k=0
    L1.append('.')
    while L1[k] !='.':
        print(L1[k])
        k+=1