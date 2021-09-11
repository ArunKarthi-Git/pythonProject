if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the Character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    L1=[]
    i=j=0
    while L[j]!='.':
        if j==0:
            L1.append(j)
        if L[j] =='\\n':
            L1.append(j+1)
        j+=1
    L1.append('-1')
    print(L1)
    m=int(input("Enter the mth line to start print"))
    n=int(input("Enter the nth line to start print"))
    i=L1[m]
    j=L1[n-1]
    while i < j:
        if L[i] !='\\n':
            print(L[i])
        i+=1
