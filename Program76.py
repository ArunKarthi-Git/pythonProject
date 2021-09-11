if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter a sentence"))
    while L[i] !='$':
        i+=1
        L.append(input())
    L[i]='.'
    i=0
    while L[i] !='.':
        print(L[i])
        i+=1
