if __name__=='__main__':
    def evenOrOdd(a):
        if a % 2 ==0:
            return "Given No. is Even"
        else:
            return "Given No is Odd"

    a=int(input("Enter a No."))
    print(evenOrOdd(a),a)