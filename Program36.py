if __name__ == '__main__':
    a=ord(input("Enter the character"))
    if a>=97 and a<=122:
        a=a-32
        print("Lower value is converted in upper",chr(a))
    else:
        print("Entered value is upper",chr(a))
