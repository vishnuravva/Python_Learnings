print("===== Finance Tracker =====")
def createTransaction():
    transaction = dict()
    print("Enter Transaction type:\nI - Income\nE - Expense")
    
    isValidType = False
    while not isValidType:
        utype = input()
        if utype.lower() == "e":
            transactionType = "Expense"
            isValidType = True
        elif utype.lower() == "i":
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
    isValidCategory = False
    while not isValidCategory:
        category = input()
        if category.strip() != "":
            isValidCategory = True
        else:
            print("Category cannot be empty")
    
    print("Enter description")
    desc = input()
    transaction["type"] = transactionType
    transaction["category"] = category.strip()
    transaction["amount"] = amount
    transaction["description"] = desc
    transactions.append(transaction)

def viewTransactions(transactions):
    if transactions:
        print(f"{'T_no':<5} | {'Type':<12} | {'Category':<12} | {'Amount':<15} | {'Description':<15}")
        print("-" * 70)
        for index, t in enumerate(transactions):
            print(f"{index + 1:<5} | {t['type']:<12} | {t['category']:<12} | {t['amount']:<15} | {t['description']:<15}")
        print("\n")
    else:
        print("No transactions recorded.")

def calcTotal():
    print("---------- Financial Summary ----------\n")
    incomeTotal = 0
    expensesTotal = 0
    expenseEntries = 0
    highestExpenseAmount = 0
    if transactions:
        for t in transactions:
            if t["type"] == "Income":
                incomeTotal += t['amount']
            elif t["type"] == "Expense":
                expensesTotal += t["amount"]
                expenseEntries+=1
                if t["amount"] > highestExpenseAmount:
                    highestExpenseAmount = t["amount"]

        balance = incomeTotal - expensesTotal  
        try:
            avgExpense = expensesTotal / expenseEntries
        except ZeroDivisionError:
            avgExpense = 0
                
        print(f"Transactions: {len(transactions)}\n")
        print(f"Expenses: {expensesTotal}")     
        print(f"Income: {incomeTotal}")    
        print(f"Balance: {balance}\n")
        print(f"Highest Expense: {highestExpenseAmount}")
        print(f"Average Expense: {avgExpense}\n")     
    else:
       print("Kindly add income / expenes to view analysis.")
    
def delTransaction():
    if transactions:
        viewTransactions(transactions)
        print("Kindly enter valid Transaction No to delete")
        
        while True:
            try:
                tNo = int(input())
                if tNo > 0 and tNo <= len(transactions):
                    deletedTransaction = transactions[tNo - 1]
                    del transactions[tNo - 1]
                    print(f"Deleted Transaction of Amount:{deletedTransaction['amount']}\nCategory:{deletedTransaction['category']}\nType:{deletedTransaction['type']}\nDescription:{deletedTransaction['description']}")
                    break
                else:
                    print("Enter valid transaction number to delete")
            except ValueError:
                print("Enter a valid transaction number")
        
    else:
        print("Kindly record transactions.")
        
def searchByCategoryFunc():
    searches = list()
    if transactions:
        print("Enter a category to search")
        searchByCategory = input()
        for t in transactions:
            if searchByCategory.lower() in t["category"].lower():
                searches.append(t)
        
        if len(searches) > 0:
            viewTransactions(searches)
        else:
            print("No transactions for this category.")
            
    else:
        print("Kindly record transactions.")
         
transactions = list()
while(True):
    print("Kindly select from the following options.")
    print("1. Add Income / Expense\n2. View Income / Expenses\n3. Calculate Total\n4. Search by Category\n5. Delete Transaction\n6.Exit\n")
    try:
        option = int(input())
        match option:
            case 1:
                createTransaction()
            case 2:
                viewTransactions(transactions)
            case 3:
                calcTotal()
            case 4:
                searchByCategoryFunc()
            case 5:
                delTransaction()
            case 6:
                break
            case _:
                print("Invalid option. Kindly select between 1-6")
    except ValueError:
        print("Invalid input. Kindly enter between 1-6 ") 
