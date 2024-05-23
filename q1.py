balance = int(input("Enter the inital balance: "))

while True:
    transaction = input("Transaction type and amount (\"done 0\"): ").split()  
    transactionType = transaction[0]
    amount = int(transaction[1])

    if transactionType == "done" and transaction[1] == '0':
        break
    
    if transactionType not in ['D', 'W'] or amount < 0:
        print("Invalid transaction!")
        continue
    
    if transactionType == "D":
        balance += amount
        print("> Deposit = %d THB, current balance = %d" % (amount, balance))
    elif transactionType == "W":
        if amount > balance:
            print("Invalid transaction!")
            continue
        balance -= amount
        print("> Withdrawal = %d THB, current balance = %d" % (amount, balance))
    
print("> Current balance = %d THB." % balance)
