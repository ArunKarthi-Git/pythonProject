if __name__=="__main__":
    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    print(i1)
    L[i1]='.'
    n=int(input("Enter the n character"))
    m=int(input("Enter the mth position to print"))
    L1=[]
    j=0
    for i1 in range(m,len(L)):
        if j < n:
            L1.append(L[i1])
            j+=1
    print(L1)