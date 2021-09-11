if __name__=='__main__':
    i=0
    L=[]
    L.append(input("Enter the character"))
    while L[i] != ' ':
        L.append(input())
        i+=1

    i=0
    while L[i] != ' ':
        print(L[i])
        i+=1