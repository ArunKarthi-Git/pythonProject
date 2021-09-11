if __name__ == '__main__':
    a=int(input("Enter the first no."))
    b=int(input("Enter the second no."))
    c=int(input("Enter the third no."))
    d=int(input("Enter the fouth no."))
    big1=a if a> b else b
    big2=big1 if big1 > c else c
    big3=big2 if big2 > d else d
    print("the biggest no. is",big3)

