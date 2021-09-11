if __name__=='__main__':
    L=[]
    i=0
    L.append(input("Enter the character"))
    while L[i] != '.':
        i += 1
        L.append(input())
    L.append('\.')
    i=0
    while L[i] !='\.':
        print(L[i])
        i+=1
