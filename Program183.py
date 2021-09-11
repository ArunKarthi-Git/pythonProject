import sys

# python Program183.py /home/karthi/Document/file10.txt /home/karthi/Document/file11.txt /home/karthi/Document/file12.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=4:
        print("Argument is not Matching")

    f1=open(sys.argv[1],'r')
    if f1 == None:
        print("file is not open or available")
        sys.exit(1)
    f2 = open(sys.argv[2], 'r')
    if f2 == None:
        print("file is not open or available")
        sys.exit(1)
    f3 = open(sys.argv[3], 'a')
    if f3 == None:
        print("file is not open or available")
        sys.exit(1)
    a=True
    while a:
        fl=f1.read()
        if not fl:
            print("End Of File")
            a = False
        f3.write(fl)
        fl=f2.read()
        if not fl:
            print("End Of File")
            a = False
        f3.write(fl)
    f1.close()
    f2.close()
    f3.close()



