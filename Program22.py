if __name__ == '__main__':
    digit =int(input("Enter the digit"))
    if(digit >0 and digit < 10):
        print("The given digit  {0} is single".format(digit))
    elif(digit >9 and digit < 99):
        print("The given digit  {0} is double".format(digit))
    else:
        print("The given digit  {0} is three".format(digit))
