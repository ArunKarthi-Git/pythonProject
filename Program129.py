if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the no.")))
    ps=0
    for j in range(len(L)):
        ps=j if L[j]<L[ps] else ps

    pb=0
    for j in range(len(L)):
        pb=j if L[j] > L[pb] else pb

    t=L[ps]
    L[ps]=L[pb]
    L[pb]=t

    for j in range(len(L)):
        print(L[j])