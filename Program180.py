import sys
# python Program180.py /home/karthi/Document/file10.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if(argc !=2):
        print("Argument not matching")
        sys.exit(1)
    fp=open(sys.argv[1],"r")
    if(fp==None):
        print("File not found")
    a=True
    while a:
        fl=fp.readline()
        if not fl:
            print("EoF")
            a=False
        print(fl)
    fp.close()


