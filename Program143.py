if __name__=='__main__':
    L=[]
    i=100
    L.append(input(""))
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    L[i1]='.'
    L1=[]
    n=int(input("Enter the no. to copy"))
    for i1 in range(n):
        L1.append(L[i1])

    for i1 in range(len(L1)):
        print(L1[i1])

    print(L1)




