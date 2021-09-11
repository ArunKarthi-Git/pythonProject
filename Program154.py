if __name__=='__main__':
    L=[]
    i=100;
    L.append(input())
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    L[i1]='.'
    L1=[]
    for i1 in range(len(L)):
        if L[i1]!='.':
            if L[i1]=='\\n':
              L1.append(i1)
            else:
                continue
    print(L1)