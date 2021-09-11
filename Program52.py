if __name__=='__main__':
    a=int(input("Enter a value:"))
    sumPostive=sumNegative=sumZero=0
    CountPostive=CountNegative=CountZero=0
    while a != -100:
        if a>0:
            sumPostive+=a
            CountPostive+=1
        elif a<0:
            sumNegative+=a
            CountNegative+=1
        else:
            sumZero+=a
            CountZero+=1
        a=int(input("Enter a value:"))
    meanPostive=sumPostive/CountPostive
    meanNegative=sumNegative/CountNegative
    print("The Mean of Postive No. is:",meanPostive)
    print("The Mean of Negative No. is:", meanNegative)
