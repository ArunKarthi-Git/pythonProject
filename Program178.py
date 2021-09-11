import sys
# python Program178.py /home/karthi/Document/file10.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if (argc!=2):
        print("Argument is not matching")
        sys.exit(1)
    fp = open(sys.argv[1], "w")
    if fp == None :
        print("file is not open or available")
        sys.exit(1)
    ch=input("Enter the character")
    while ch !='$':
        fp.write(ch)
        ch=input("Enter the character")

    fp.close()