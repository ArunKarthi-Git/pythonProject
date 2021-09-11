if __name__=='__main__':
    i=3
    j=3
    k=3

    M1=[]
    for i1 in range(i):
        M=[]
        for j1 in range(j):
            M.append(int(input()))
        M1.append(M)

    M2=[]
    for i1 in range(i):
        M=[]
        for j1 in range(j):
            M.append(int(input()))
        M2.append(M)
    M4=[]
    for i1 in range(i):
        M3 = []
        for j1 in range(j):
                M3.append(M1[i1][j1]*M2[i1][j1])
        M4.append(M3)

    for i1 in range(i):
        for j1 in range(j):
            print(M4[i1][j1],end=" ")
        print()