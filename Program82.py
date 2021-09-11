if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the Character"))
    while L[i]!='$':
        i+=1
        L.append(input("Enter the Character"))
    L[i]='.'

    n=int(input("Enter the last n character to copy"))
    L1=[]
    i=i-n
    while L[i]!='.':
        L1.append(L[i])
        i+=1
    L1.append('.')
    k=0
    while L1[k]!='.':
        print(L1[k])
        k+=1