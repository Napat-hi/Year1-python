n = int(input("Enter an integer number (n>0): "))
if n >= 0:
    choice = int(input("""(1) Factorial of n (n!)
          (2) Summation of n integers
          Select operation: """))

    if choice == 1:
        fact = 1
        for i in range(1, n+1):
            fact *= i

        print("Factorial of %d (%d!) = %d" % (n, n, fact))

    elif choice == 2:
        sum = 0
        for i in range(1, n+1):
            sum += i
            
        print("Summation of n integers = %d " % (sum))

    else:
        print("N/A Operation!")


else:
    print("you suck")