if __name__=='__main__':
    L=[]
    i=3
    j=3
    for i1 in range(i):
        a=[]
        for ji in range(j):
            a.append(int(input()))
        L.append(a)

    L1=[]
    for i1 in range(i):
        b=[]
        for j1 in range(j):
            b.append(int(input()))
        L1.append(b)

    L3=[]
    for i1 in range(i):
        L4=[]
        for j1 in range(j):
            L4.append(L[i1][j1]+L1[i1][j1])
        L3.append(L4)

    for i1 in range(i):
        for j1 in range(j):
            print(L3[i1][j1],end=" ")
        print()