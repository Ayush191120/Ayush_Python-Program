# Each transaction stores amount and running balance
# Handles both credits (positive) and debits (negative)

# Detailed Output:
# Well-formatted transaction table with columns
# Clear distinction between credits and debits
# Running balance shown after each transaction

# Comprehensive Summary:
# Shows total credits and debits
# Displays final balance
# Counts total transactions


def bank_transaction_analyzer():
    transactions = []
    balance = 0

    print("Enter your transactions (type 'done' to finish):")
    print("Format: credit 1000 OR debit 500")

    while True:
        entry = input("> ").strip().lower()
        if entry == 'done':
            break

        try:
            t_type, amount = entry.split()
            amount = float(amount)

            if t_type == 'credit':
                balance += amount
                transactions.append(('Credit', amount, balance))
            elif t_type == 'debit':
                balance -= amount
                transactions.append(('Debit', amount, balance))
            else:
                print("Invalid transaction type. Use 'credit' or 'debit'.")
        except ValueError:
            print("Invalid format. Use: credit 1000 OR debit 500")

    print("\nTransaction Summary:")
    print("{:<10} {:<10} {:<10}".format("Type", "Amount", "Balance"))
    print("-" * 30)
    for t_type, amount, bal in transactions:
        print(f"{t_type:<10} ₹{amount:<9.2f} ₹{bal:<.2f}")
    print("-" * 30)
    print(f"Final Balance: ₹{balance:.2f}")

# Run the program
bank_transaction_analyzer()
