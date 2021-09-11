if __name__=='__main__':
    L=[]
    i=10
    for j in range(i):
        L.append(int(input("Enter the No.")))


    ps=0
    pb=0
    for j in range(len(L)):
        ps=j if L[j] < L[ps] else ps

    for j in range(len(L)):
        pb=j if L[j] > L[pb] else pb

    print("The postiton of Smallest No. is",ps+1)
    print("The postiton of Biggest No. is", pb+1)