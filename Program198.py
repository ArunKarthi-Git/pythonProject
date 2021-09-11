import sys
# python Program190.py /home/karthi/Document/file11.txt
if __name__=="__main__":
    argc=len(sys.argv)
    if argc !=2:
        print("Argument is not valid")
        sys.exit(1)
    L=[]
    L.append(input("Enter the Name"))
    L.append(int(input("Enter the age")))
    L.append(float(input("Enter the Salary" )))

    f=open(sys.argv[1],"w")
    List_len=len(L)
    for i in range(0,List_len):
        f.write(str(L[i])+" ")
    f.close()

