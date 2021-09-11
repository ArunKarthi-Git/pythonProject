if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the Character"))
    while L[i] != '$':
        i+=1
        L.append(input("Enter the Character"))

    L[i]='.'
    i=0
    C=[]
    while L[i] !='.':
      C.append(L[i])
      i+=1
    print(L)
    print(C)

