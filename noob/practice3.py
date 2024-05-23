print("Multiplication table:")
game = int(input("Please enter a number between 1 to 25 :"))
if 1 <= game <= 25:
    print("Multiplication table of %d " % game)

    for i in range(1, 13):
        print("%d x %d = %d" % (game, i, game*i))


else:
    print("You entered invalid number")
