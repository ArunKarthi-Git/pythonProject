if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the no.")))
    big=0

    for j in range(len(L)):
       big=L[j] if L[j]>big else big

    print("The biggest of 10 No. is :",big)