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
    m=0
    while L[j] !='.':
        if(L[j]=='\\n' or j==0):
            m=j+1
            L1.append(m)
        j+=1
    L1.append('.')
    k=0
    while L1[k] !='.':
        print(L1[k])
        k+=1
