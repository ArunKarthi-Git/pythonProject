import sys

if __name__=='__main__':
    argc=len(sys.argv)
    if argc <3:
        print("Argument is not Matching")
        sys.exit(1)
    pattern=sys.argv[1]
    print(pattern)
    for i in range(2,argc):
        f=open(sys.argv[i],"r")
        if f is None:
            print("File not be open")
            sys.exit(1)
        l=0
        for line in f:
            l+=1
            if pattern in line:
                print(l,line)


