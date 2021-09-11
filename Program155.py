if __name__=="__main__":
    L=[]
    i=100
    L.append(input())
    for i1 in range(i):
        if L[i1]!='$':
            L.append(input())
        else:
            break
    L[i1]='.'
    n=int(input("Dispaly the n the line"))
    L1=[]
    for i1 in range(len(L)):
        print(i1)
        if i1==n:
            print(L[i1])

