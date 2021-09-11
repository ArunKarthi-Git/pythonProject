if __name__=='__main__':
    L=[]
    i=0
    while i < 10:
        L.append(int(input("Enter a No.")))
        i+=1
    i=0
    big=0
    while i < 10 :
        if L[i] > big:
            big=L[i]
        i+=1
    i=0
    sbig=0
    bpos=0
    while i < 10:
        if L[i] > sbig and L[i] !=big:
            sbig=L[i]
            bpos=i
        i+=1
    print("The Second Biggest No.",sbig)
    i=0
    small=L[i]
    while i < 10 :
        if L[i] < small:
            small =L[i]
        i+=1
    print("The first smallest No.", small)

    i = 0
    secondSmall = L[i]
    while i < 10:
        if L[i] <= secondSmall and L[i] > small:
            secondSmall = L[i]
        i += 1

    i=0
    ssmall=L[i]
    spos=0
    while i < 10:
        if L[i] < ssmall and L[i] != small:
            ssmall=L[i]
            spos=i
        i+=1
    print("The Second smallest No.", ssmall)


    temp=L[bpos]
    L[bpos]=L[spos]
    L[spos]=temp

    i=0
    while i<10:
        print(L[i])
        i+=1


    print("The second smallest No. is",L[spos],"in Postion",spos)
    print("The second larget No. is", L[bpos], "in Postion",bpos)