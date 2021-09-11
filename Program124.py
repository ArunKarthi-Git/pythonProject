if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the no.")))
    i=0
    big=0
    for j in range(len(L)):
        if L[i] > big:
            big=L[i]
        i+=1
    print("The biggest of 10 No.is:",big)