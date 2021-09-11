if __name__=='__main__':
    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1] !='$':
            L.append(input())
        else:
            break
    L[i1]='.'
    L1=[]
    for i1 in range(len(L)):

        if L[i1] !='.':
            if L[i1]==':' or L[i1]==';':
                '''i1+=1'''
                continue
            else:
                L1.append(L[i1])

    L1.append('.')
    print(L1)
    p=""
    for i1 in range(len(L1)):
        if L1[i1]!='.':
            p+=L1[i1]

    print(p)