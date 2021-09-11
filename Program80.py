if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter the character"))
    L[i]='.'
    n=int(input("Enter the copy charter"))
    i=0
    C=[]
    while i < n:
        C.append(L[i])
        i+=1
    print(L)
    print(C)