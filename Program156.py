if __name__=='__main__':
    L=[]
    i=200
    L.append(input())
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    L[i1]='.'
    m=int(input("Enter the mth line"))
    n=int(input("Enter the nth line"))
    for i1 in range(m,n):
        print(L[i1])