import sys
# python Program191.py /home/karthi/Document/file11.txt

if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=2:
        print("Argument is not Valid")
        sys.exit(1)

    f1=open(sys.argv[1],"r")
    if f1 is None:
        print("File is not found")
        sys.exit(1)

    print("Hello")
    u=l=d=s=0
    while 1:
        ch=f1.read(1)
        if not ch:
            break
        if ord(ch) >= 65 and ord(ch) <=90:
            u+=1
        elif ord(ch) >= 97 and ord(ch) <=122:
            l+=1
        elif ord(ch) >= 48 and ord(ch) <=57:
            d+=1
        else:
            s+=1
    print("The upper is",u)
    print("The lowe is", l)
    print("The digit is", d)
    print("The spl is", s)

    f1.close()

