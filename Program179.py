import sys
# python Program179.py /home/karthi/Document/file10.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=2:
        print("Argument is not matching")
        sys.exit(1)
    fp = open(sys.argv[1], "r")
    if fp == None:
        print("file is not open or available")
        sys.exit(1)

    a = True
    while a:
        file_line = fp.readline()
        if not file_line:
            print("End Of File")
            a = False
        print(file_line)
    fp.close()

