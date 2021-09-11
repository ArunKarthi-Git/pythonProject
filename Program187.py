import sys
# python Program187.py /home/karthi/Document/file11.txt
if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=2:
        print("Argument not Matched")
        sys.exit(1)

    f1=open(sys.argv[1],"w")
    if f1 is None:
        print("File cannot be open")
        sys.exit(1)
    L=[]
    L.append(input("Enter the Character"))
    i=0
    while L[i]!='$':
        L.append(input("Enter the Character"))
        i+=1
    L[i]='.'
    i=0
    while L[i]!='.':
        f1.write(L[i])
        i+=1

    f1.close()
