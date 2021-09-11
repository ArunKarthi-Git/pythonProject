if __name__=='__main__':
    L=[]
    i=0
    while i < 10:
        L.append(int(input("Enter the No.")))
        i+=1
    i=0
    small=L[i]
    while i < 10:
        if L[i] < small:
            small=L[i]
        i+=1
    i=0
    secondSmall=L[0]
    while i <10:
        if L[i] <= secondSmall and L[i] > small:
            secondSmall=L[i]
        i+=1
    print("The second smallest No. is:",secondSmall)
