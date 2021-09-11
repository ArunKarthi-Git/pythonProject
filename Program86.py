if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the Character"))
    while L[i]!='$':
        i+=1
        L.append(input("Enter the Charcter"))
    L[i]='.'
    L1=[]
    j=i-1
    while j>=0:
       L1.append(L[j])
       j-=1
    L1.append('.')
    i=0
    while L1[i]!='.':
        print(L1[i])
        i+=1

