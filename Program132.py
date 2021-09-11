if __name__=='__main__':
    L=[]
    i=3
    j=3
    for i1 in range(i):  # A for loop for row entries
        a = []
        for j1 in range(j):  # A for loop for column entries
            a.append(int(input()))
        L.append(a)

    for i1 in range(i):
        for j1 in range(j):
            print(L[i1][j1], end=" ")
        print()
