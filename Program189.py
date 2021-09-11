import sys
# python Program189.py /home/karthi/Document/file11.txt
if __name__=='__main__':
    argc=len(sys.argv)

    if argc!=2:
        print("Argument is not Valid")
        sys.exit(1)

    f1=open(sys.argv[1],"r")
    if f1 is None:
        print("File Cannot be open")
        sys.exit(1)


    TempList=[]
    lines = f1.readlines()
    l=0
    for line in lines:
        l=l+1
        print(l,line)

        '''a = True
        l = 0
        while a:
            fline = f1.read(1)
            if not fline:
                print("EOF")
                a = False
                sys.exit(1)
            if fline == '\n':
                l = l + 1
                print(l, lines)
                #TempList.clear()
        # TempList.append(fline)
    '''


