import sys
# python Program184.py /home/karthi/Document/file10.txt /home/karthi/Document/file11.txt
if __name__=="__main__":
    argc=len(sys.argv)

    if argc !=3:
        print("Argument is not validate")
        sys.exit(1)

    f1=open(sys.argv[1],"r")
    f2=open(sys.argv[2],"w")
    if f1==None or f2 == None:
        print("file is not open")
        sys.exit(1)
    a=True
    while a:
        fl=f1.read(1)
        if not fl:
            print("File is end")
            a=False
        print(fl)
        f2.write(chr(ord(fl)+1))
    f1.close()
    f2.close()