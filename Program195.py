import sys

# python Program195.py /home/karthi/Document/file11.txt

if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=3:
        print("Argument is not match")
        sys.exit(1)
    file1=open(sys.argv[2],"r")
    if file1 is None:
        print("fiile is not found")
        sys.exit(1)

    string1=sys.argv[1]
    # setting flag and index to 0
    flag = 0
    index = 0

    # Loop through the file line by line
    for line in file1:
        index+=1
        # checking string is present in line or not
        if string1 in line:
            flag = 1
            print('String', string1, 'Found In Line', index)
            continue

            # checking condition for string found or not
    '''if flag == 0:
        print('String', string1, 'Not Found')
    else:
        print('String', string1, 'Found In Line', index)'''

    # closing text file
    file1.close()
