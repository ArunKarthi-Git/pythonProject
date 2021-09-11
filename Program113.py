if __name__=='__main__':
    L=[]
    L.append(int(input("Enter the No.")))
    j=0
    sumPostive=0
    sumNegative = 0
    for i in L:
        if i != -100:
            if i >0:
                sumPostive+=i
            else:
                sumNegative += i
        else:
            continue
        L.append(int(input("Enter the no.")))
    print(sumPostive)
    print(sumNegative)

