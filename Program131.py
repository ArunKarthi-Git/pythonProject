if __name__=='__main__':

    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the No.")))

    pb1=0
    big1=0
    for j in range(len(L)):
        pb1=j if L[j] > L[pb1] else pb1

    print("The Position of i st biggest No. is:",pb1)
    pb2=0
    big2=0
    for j in range(len(L)):
        pb2=j if L[j] > L[pb2] and L[j] != L[pb1] else pb2

    ps1=0
    small1=0
    for j in range(len(L)):
        ps1=j if L[j] < L[ps1] else ps1

    ps2=0
    small2=0
    for j in range(len(L)):
        ps2 =j if L[j] < L[ps2] and L[j] != L[ps1] else ps2

    t=L[ps2]
    L[ps2]=L[pb2]
    L[pb2]=t

    for j in range(len(L)):
        print(L[j])



