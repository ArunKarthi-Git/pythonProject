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
    k1=0
    #for k1 in range(k,len(L)):
    while k1 <= len(L)-1:
        n=k1
        m=0
        for m1 in range(m,len(L1)):
            print(L1[m1],"=",L[n])
            if L1[m1]==L[n] and L1[m1]!='.':
                n+=1
                continue
            if L1[m1] == '.':
                k1 = n
                #L2.append(L[k1])
                break
            if L1[m1] != L[n] and L1[m1] != '.':
                L2.append(L[k1])
                k1+=1
                break
print("The deleted pattern is",L2)

