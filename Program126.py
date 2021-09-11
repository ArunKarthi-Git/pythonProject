if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the no.")))
    big=0
    p=0
    for j in range(len(L)):
        if L[j] > big:
            big=L[j]
            p=j+1
    print("The biggest no.of position is:",p)