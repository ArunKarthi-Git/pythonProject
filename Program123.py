if __name__=='__main__':
    L=[]
    i=10
    mean=0
    sum=0
    for j in range(i):
        L.append(int(input("Enter the No.")))
    i=10
    for j in range(i):
        sum+=L[j]

    print(sum,j)
    mean=sum/j+1
    print("Mean of 10 no. is:",mean)