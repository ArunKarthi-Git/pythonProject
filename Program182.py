import sys
# python Program182.py /home/karthi/Document/file10.txt /home/karthi/Document/file11.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if argc != 3:
        print("Arugment are required")
        sys.exit(1)
    f1=open(sys.argv[1],'r')
    if f1 == None:
        print("file is not open or available")
        sys.exit(1)
    f2=open(sys.argv[2],'w')
    if f2 == None:
        print("file is not open or available")
        sys.exit(1)
    a = True
    while a:
        fl = f1.read()
        if not fl:
            print("End Of File")
            a = False
        print(fl)
        f2.write(fl)
    f1.close()
    f2.close()
