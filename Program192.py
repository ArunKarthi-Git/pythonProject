import sys
# python Program192.py /home/karthi/Document/file11.txt

if __name__=='__main__':
    argc=len(sys.argv)
    if argc !=2:
        print("Argument is not Valid")
        sys.exit(1)

    f1=open(sys.argv[1],"r")
    if f1 is None:
        print("File is not found")
        sys.exit(1)

    num_words = 0
    num_lines = 0
    num_charc = 0
    num_spaces = 0
    with open(sys.argv[1], "r") as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif (letter == ' '):
                    num_spaces += 1
                    word = 'Y'
                for i in letter:
                    if (i != " " and i != "\n"):
                        num_charc += 1

    # printing total word count
    print("Number of words in text file: ", num_words)

    # printing total line count
    print("Number of lines in text file: ", num_lines)

    # printing total character count
    print('Number of characters in text file: ', num_charc)

    # printing total space count
    print('Number of spaces in text file: ', num_spaces)

    f1.close()

