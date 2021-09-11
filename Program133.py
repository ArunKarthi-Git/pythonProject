if __name__=="__main__":
    L=[]
    i=3
    j=3
    for i1 in range(i):
        a=[]
        for ji in range(j):
            a.append(int(input()))
        L.append(a)

    for i1 in range(i):
        for j1 in range(j):
            print(L[j1][i1], end=" ")
        print()


