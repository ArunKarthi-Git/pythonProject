import sys
# python Program188.py /home/karthi/Document/file11.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=2:
        print("Argument not Matched")
        sys.exit(1)

    f1=open(sys.argv[1],"r")
    if f1 is None:
        print("File cannot be open")
        sys.exit(1)

    L=[]
    while 1:
        # read by character
        char = f1.read(1)
        if not char:
            break
        L.append(char)

    L.append('.')
    i=0
    while L[i]!='.':
        print(L[i])
        i+=1
    f1.close()
