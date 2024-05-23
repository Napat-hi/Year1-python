def print_isosceles_triangle(num):
    for i in range(1, num + 1):
        spaces = " " * (num - i)
        stars = str(i) * (2 * i - 1)
        print(spaces + stars)



while True:
    try:
        user_input = int(input("Enter an integer (0 to exit): "))
    except ValueError:
        print("Invalid input!")
        continue

    if user_input == 0:
        print("Exit program. Bye!")
        break

    if 0 <= user_input <= 9:
        print_isosceles_triangle(user_input)
    else:
        print("Invalid input!")

