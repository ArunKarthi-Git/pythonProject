if __name__=='__main__':
    L=[]
    L.append(int(input("Enter the No.")))

    j=0
    countPostive=0
    countNegative=0
    countZero=0
    for i in L:
        if i != -100:
            if L[j] > 0:
                countPostive+=1
            elif L[j] <0:
                countNegative+=1
            else:
                countNegative+=1
        else:
            continue
        j+=1
        L.append(int(input("Enter the No.")))
    print("The No. of Positive count is",countPostive)
    print("The No. of Negative count is", countNegative)
    print("The No. of Zero count is", countZero)

