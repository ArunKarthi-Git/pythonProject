if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the no.")))
    big=0
    pb=0
    for j in range(len(L)):
        print(L[j],"---",L[pb])
        print(j,"---------",pb)
        pb=j if L[j] > L[pb] else pb

    print("The postion of biggest no. is:",pb+1)

