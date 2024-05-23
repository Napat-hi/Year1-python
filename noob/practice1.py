days = int(input("Input number of days:"))
hours = int(input("Input number of hour1:"))

print("Please select a choice:")
choice = int(input("""
#              1-to calculate the total number of second or
#              2-to calculate the total number of minutes:
#              Enter your selected choice:"""))

print('----------------------------------------------')


if (choice == 1):
    print("The total number of minutes are %d." % (((days*24)+hours)*60*60))
elif(choice == 2):
    print("The total number of minutes are %d." % (((days*24)+hours)*60))
