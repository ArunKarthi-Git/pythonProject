if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the No.")))

    big=0
    for j in range(len(L)):
        big=L[j] if L[j] > big else big

    big2=0
    for j in range(len(L)):
        big2=L[j] if L[j] > big2 and L[j] != big else big2

    print("The second biggest No.:",big2)