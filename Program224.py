import sys

if __name__ =='__main__':

    def file(f1):
        ch=input("Enter the character")
        while ch !='$':
            f1.write(ch)
            ch=input("Enter the character")


    argc = len(sys.argv)
    if argc != 2:
        print("Argument is not valid")
        sys.exit(1)
    f=open(sys.argv[1],"w")
    file(f)
