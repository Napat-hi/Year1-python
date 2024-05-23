count = 0
sum = 0

while True:
    number = int(input("Enter an integer (-1 to quit):"))
    if number == -1:
        break
    
    count += 1
    sum += number

print("Number of inputs:", count)
print("Sum of numbers:", sum)
    
