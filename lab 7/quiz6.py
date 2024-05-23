while True:
    print("===== MAIN MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")

    choice = input("Select an operation (1-3):")
    if choice == '1':
        number = input("Enter two number:").split()
        result = int(number[0]) + int(number[1])
        print(f"{number[0]}+{number[1]} = {result}")
    elif choice == '2':
        number = input("Enter two number:").split()
        result = int(number[0]) - int(number[1])
        print(f"{number[0]}-{number[1]} = {result}")
    elif choice == '3':
        print("Bye!!!")
        break
    else:
        print("Invalind choice. Please select a vaild optain(1-3).")
        continue
