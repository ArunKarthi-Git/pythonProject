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
        if L[i1]=='':
            L1.append(" ")
            i1+=1
        elif ord(L[i1]) >64  and ord(L[i1]) < 97:
            L1.append(chr(ord(L[i1]) + 32))
        else:
            L1.append(L[i1])


    for i1 in range(len(L1)):
         print(L1[i1])

    print(L1)