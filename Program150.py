if __name__=='__main__':

    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    L1=[]
    i=100
    L1.append(input())
    for i1 in range(i):
        if L1[i1]!='$':
            L1.append(input())
        else:
            break
    L2=[]
    for i1 in range(len(L)-1):
        L2.append(L[i1])
    for i1 in range(len(L1)-1):
        L2.append(L1[i1])

    print(L2)