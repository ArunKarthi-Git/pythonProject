if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    l=i=j=0
    L1=[]
    while L[j] !='.':
       if j==0:
           L1.append(j)
       if L[j] =='\\n':
           L1.append(j+1)
       j+=1
    L1.append('-1')
    n=int(input("Enter the number to print the line"))
    k=L1[n-1]
    while L[k]!='\\n':
        print(L[k])
        k+=1

