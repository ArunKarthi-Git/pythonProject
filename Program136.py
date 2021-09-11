if __name__=='__main__':
    L=[]
    L.append(input("Enter the Character"))
    i1=100
    for i in range(i1):
        if L[i] !=' ':
            L.append(input("Enter the Character"))
        else:
            break
    L[i]='.'
    for i in range(len(L)-1):
        print(L[i])