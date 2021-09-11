import sys
# python Program190.py /home/karthi/Document/file11.txt
if __name__=="__main__":
    argc=len(sys.argv)
    if argc !=2:
        print("Argument is not valid")
        sys.exit(1)

    L=[]
    f=open(sys.argv[1],"r")
    for i in f:
        L.append(i)
    for i in range(0, len(L)):
        print(L[i])
