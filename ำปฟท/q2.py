n = input("Input: ")

if n.isdigit():
    n = int(n)

    if 1 <= n <= 15:
        current_value = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j < i:
                    print("0", end="\t")
                else:
                    print(current_value, end="\t")
                    current_value += 1
            print()

    else:
        print("Invalid input")
        exit()
else:
    print("Invalid input")
    exit()