even = 0
odd = 0

while True:
    number = int(input("Enter an integer (0 to exit):"))
    if number == 0 :
       break 
    
    if number % 2 == 0:
        even += 1
    else :
        odd += 1
print("----------------------------------------")    
print("The number of even integers is",even)
print("The number of odd integers is",odd)

    