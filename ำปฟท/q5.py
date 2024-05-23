number = input("Input: ")
number = int(number)

if 1 <= number <= 15 :
    current_value = 1
    for r in range(1,number+1) :
        for c in range(1,number+1):
            if c<r :
                print("0", end="\t")
            else:
                print(current_value, end="\t") 
                current_value += 1

        print()
else :
    print("Invalid input")
    