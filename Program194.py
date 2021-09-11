import sys
# python Program194.py /home/karthi/Document/file11.txt
if __name__=='__main__':
    argc=len(sys.argv)

    if argc !=3:
        print("Argument is not matching")
        sys.exit(1)

    word=sys.argv[1]
    file=open(sys.argv[2],"r")
    readfile = file.read()
    #for check in readfile:
        #print(check)
    if word in readfile:
        print("Pattern Exit",word)
    file.close()
