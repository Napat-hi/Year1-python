print("=====================")
print("Cashier Program")
print("=====================")

count = 0
sum = 0

while True:
    number = float(input("Enter item price or -1 when finished:"))
    if number == -1:
        break
    
    count += 1
    sum += number
    
print("\nTotal purchase amount is", sum)

money = int(input("\nYour payment:"))
print("\nYou bought %d items today."%count)
total = money-sum
print("Your change is %.2f bath."%total)
