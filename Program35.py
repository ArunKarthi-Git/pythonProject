if __name__ == '__main__':
    a = ord(input("Enter the character"))
    if a>=65 and a<=90:
        a = a + 32
        print("The Given character is converted into lower",chr(a))
    else:
        print("The Given character is lower",chr(a))
