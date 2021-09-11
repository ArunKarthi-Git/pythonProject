if __name__=='__main__':
    L=[]
    i=100
    L.append(input("Enter the char"))
    for i1 in range(i):
        if L[i1] !='$':
            L.append(input("Enter the char"))
        else:
            break
    L[i1]='.'
    for i1 in range(len(L)-1):
        print(L[i1])
