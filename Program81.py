if __name__=='__main__':
    L=[]
    L.append(input("Enter the Character"))
    i=0
    while L[i] !='$':
        i+=1
        L.append(input("Enter the Character"))
    L[i]='.'
    n=int(input("Enter the no. of character to copy"))
    m=int(input("Enter the no. from which character to copy"))
    L1=[]
    i=0
    while i<=n:
        L1.append(L[i])
        i += 1
        m +=1
    L1.append('.')
    i=0
    while L1[i]!='.':
        print(L1[i])
        i+=1