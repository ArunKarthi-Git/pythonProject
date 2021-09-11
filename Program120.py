if __name__=='__main__':
    L=[]
    i=10
    sum=0
    mean=0
    for j in range(i):
        L.append(int(input("Enter the no.")))
        sum+=L[j]
    mean=sum/j
    print("Mean of 10 no. is:",mean)

