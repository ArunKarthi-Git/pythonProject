if __name__=='__main__':
    firstNo=int(input("Enter First No.:"))
    secondNo = int(input("Enter Second No.:"))
    thirdNo = int(input("Enter Third No.:"))
    if (firstNo > secondNo) and (firstNo > thirdNo):
        print("The Biggest No is:",firstNo)
    elif (secondNo > firstNo) and (secondNo > thirdNo):
        print("The Biggest No is:", secondNo)
    else:
        print("The Biggest No is:", thirdNo)

