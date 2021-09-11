import sys
# python Program181.py /home/karthi/Document/file10.txt /home/karthi/Document/file11.txt
if __name__=="__main__":
    argc=len(sys.argv)
    if argc < 2:
        print("Argument is not matching")
        sys.exit(1)
    i=argc
    for i1 in range(1,i):
       fp=open(sys.argv[i1])
       print(sys.argv[i1])
       if fp == None:
           print("file is not open or available")
           sys.exit(1)
       a=True
       while a:
           fl=fp.read()
           if not fl:
               print("End Of File")
               a = False
           print(fl)
       fp.close()