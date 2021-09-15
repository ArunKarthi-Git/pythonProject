if __name__=='__main__':
    L=[]
    i=5
    sum=0
    mean=0
    for j in range(i):
        L.append(int(input("Enter the no.")))
        sum+=L[j]
    total=len(L)
    mean=sum/total
    print("Mean of 5 no. is:",mean)

