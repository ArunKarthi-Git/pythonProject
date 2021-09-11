if __name__=="__main__":
    a=int(input("Enter a value:"))
    postive=negative=zero=0
    while a !=-100:
        if a > 0:
            postive +=1
        elif a < 0:
            negative +=1
        else :
            zero +=1
        a=int(input("Enter a value:"))
    print("Count of positive No. is:",postive)
    print("Count of negative No. is:", negative)
    print("Count of Zero  is:", zero)
