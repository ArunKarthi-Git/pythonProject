if __name__=='__main__':
    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1] !='$':
            L.append(input())
        else:
            break
    L1=[]
    for i1 in range(len(L)):
        if L[i1]==',':
            continue
        else:
            L1.append(L[i1])

    print(L1)