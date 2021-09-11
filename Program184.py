import sys
# python Program184.py /home/karthi/Document/file10.txt /home/karthi/Document/file11.txt
if __name__=="__main__":
    argc=len(sys.argv)

    if argc!=3:
        print("Argument is not valid")
        sys.exit(1)

    f1=open(sys.argv[1],"r")
    if f1 == None:
        print("File cannot be open")
        sys.exit(1)

    f2 = open(sys.argv[2], "w")
    if f2 == None:
        print("File cannot be open")
        sys.exit(1)

    a=True
    while a:
        fl=f1.read(1)
        if not fl:
            print("End of file")
            a=False
        if ord(fl) >= 65 and ord(fl)<= 90:
            f2.write(chr(ord(fl)+32))
        else:
            f2.write(fl)
    f1.close()
    f2.close()
