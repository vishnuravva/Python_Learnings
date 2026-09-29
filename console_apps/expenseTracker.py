print("===== Expense Tracker =====")
def createTransaction():
    transaction = dict()
    print("Enter Transaction type:\nI - Income\nE - Expense")
    
    isValidType = False
    while not isValidType:
        utype = input()
        if utype == "E":
            transactionType = "Expense"
            isValidType = True
        elif utype == "I":
            transactionType = "Income"
            isValidType = True
        else:
            print("Enter Transaction type:\nI - Income\nE - Expense")

    print("Enter Amount")
    isValidAmount = False
    while not isValidAmount:
        try:
            amount = float(input())
            if amount > 0:
                isValidAmount = True
            else:
                print("Amount should be > 0")
        except ValueError:
            print("Enter valid amount")
    print("Enter a category")
    category = input()
    print("Enter description")
    desc = input()
    if(isValidAmount and isValidType):
        transaction["type"] = transactionType
        transaction["category"] = category
        transaction["amount"] = amount
        transaction["description"] = desc
        transactions.append(transaction)

def viewTransactions():
    if transactions:
        print(f"{'Type':<12} | {'Category':<12} | {'Amount':<15} | {'Description':<15}")
        print("-" * 70)
        for t in transactions:
            print(f"{t['type']:<12} | {t['category']:<12} | {t['amount']:<15} | {t['description']:<15}")
        print("\n")
    else:
        print("No transactions recorded.")
        
transactions = list()
while(True):
    print("Kindly select from the following options.")
    print("1. Add Income / Expense\n2. View Income / Expenses\n3. Calculate Total\n4. Find Highest Expense\n5. Category-wise Total\n6. Search by Category\n7. Delete Expense\n8.Exit\n")
    option = int(input())
    match option:
        case 1:
            createTransaction()
        case 2:
            viewTransactions()
        case 8:
            break
        case _:
            print("Invalid option. Kindly select between 1-8")
        
