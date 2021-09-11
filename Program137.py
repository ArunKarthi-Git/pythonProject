if __name__=='__main__':
    L=[]
    i=100
    L.append(input("Enter the Character"))
    for i1 in range(i):
        if L[i1] !='.':
            L.append(input("Enter the Character"))
        else:
            break

    L[i1]='.'
    for i1 in range(len(L)):
        print(L[i1])