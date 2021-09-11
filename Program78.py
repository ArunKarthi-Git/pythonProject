if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter a character"))
    while L[i] !='$':
        i+=1
        L.append(input("Enter a charcater"))
    L[i]='.'
    i=w=l=c=0
    while L[i]!='.':
        if L[i]!='\b' and L[i+1]=='\b':
            w+=1
        if(L[i] =='\n'):
            l+=1
        i+=1
        c=i
    print(w,l,c)
