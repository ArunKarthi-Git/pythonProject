if __name__=="__main__":
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] != '$':
        i+=1
        L.append((input("Enter the character")))
    L[i]='.'
    L1=[]
    j=0
    k=1
    while L[j] !='.':
        if(L[j]==':' or L[j]==';'):
            k+=1
        else:
            L1.append(L[j])
        j+=1
    L1.append(".")
    l=0
    '''while L1[l] !='.':
        print(L1[l])
        l+=1'''
    print(L1)


