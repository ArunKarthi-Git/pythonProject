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
    L1.append(L[len(L)-1:None:-1])
    print(L[len(L)-1:None:-1])

    L2=[]
    for i1 in range(len(L1)):
        print(L1[i1])



