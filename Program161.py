if __name__=='__main__':
    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    L[i1]='.'

    L1=[]
    j=100
    L1.append(input())
    for j1 in range(j):
        if L1[j1]!='$':
            L1.append(input())
        else:
            break

    L1[j1]='.'
    L2=[]
    j = 100
    L2.append(input())
    for j1 in range(j):
        if L2[j1] != '$':
            L2.append(input())
        else:
            break
    L2[j1] = '.'

    L3=[]
    k=0
    #for k in range(k,len(L)-1):
    while k < len(L):
        l=k
        m=0
        print("k=",k)
        for m1 in range(m,len(L1)):
            print(L1[m1],"==",L[l])
            if L1[m1] == L[l] and L1[m]!='.':
                l+=1
                continue
            if L1[m1]=='.':
                o=0
                for o1 in range(o,len(L2)-1):
                    L3.append(L2[o1])
                    continue
                k=l
                break
            if L1[m1] != L[l] and L1[m1] != '.':
                L3.append(L[l])
                k += 1
                break

    print(L3)



