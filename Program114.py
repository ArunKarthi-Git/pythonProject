if __name__=='__main__':
    L=[]
    sumPositive=0
    sumNegative=0
    countPositve=0
    countNegative=0
    L.append(int(input("Enter the no.")))
    j=0
    for i in L:
        if i !=-100:
            if L[j]>0:
                sumPositive+=L[j]
                countPositve+=1
            elif L[j]<0:
                sumNegative += L[j]
                countNegative+=1
        else:
            continue
        j+=1
        L.append(int(input("Enter the no.")))
    print("Mean of Positive:",sumPositive/countPositve)
    print("Mean of Negative:", sumNegative/countNegative)