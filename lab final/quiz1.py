current_balance = int(input("Enter initial balance: "))

while True:
    transaction = input(
        "Transaction type and amount (\"done 0\" to exit): ").split()
    transaction_type = transaction[0]
    amount = int(transaction[1])

    if transaction_type == 'done' and amount == 0:
        break

    if transaction_type not in ['D', 'W']:
        print("Invalid transaction type!")
        continue
    if transaction_type == 'D':
        if amount > 0:
            current_balance += amount
            print(
                f"Deposit: {amount:.2f}, Current Balance: {current_balance:.2f}")
        else:
            print("Invalid transaction!")
    elif transaction_type == 'W':
        if current_balance >= amount:
            current_balance -= amount
            print(
                f"Withdrawal: {amount:.2f}, Current Balance: {current_balance:.2f}")
        else:
            print("Invalid transaction!")


print("Current balance:%s THB" % current_balance)
