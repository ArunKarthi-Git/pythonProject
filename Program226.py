import sys

if __name__ =='__main__':

    def file(f1):
        a = True
        while a:
            fl = f1.readline()
            if not fl:
                print("EoF")
                a = False
            print(fl)



    argc = len(sys.argv)
    if argc != 3:
        print("Argument is not valid")
        sys.exit(1)
    i=1
    while i<=3:
        f=open(sys.argv[i],"r")
        file(f)
        i+=1
