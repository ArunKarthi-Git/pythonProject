if __name__=='__main__':
    year=int(input("Enter the year:"))
    if(year%4):
        print("The given year is leap",format(year))
    else:
        print("The given year is not leap",format(year))
