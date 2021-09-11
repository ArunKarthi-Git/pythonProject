import sys

if __name__=='__main__':
    argc=len(sys.argv)
    if argc <3:
        print("Argument is not Matching")
        sys.exit(1)

    for i in range(1,argc):
        f=open(sys.argv[i],"r")
        if f is None:
            print("File not be open")
            sys.exit(1)
        l=0
        for line in f:
            print(l,line)
            l+=1