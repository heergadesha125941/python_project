import matplotlib.pyplot as plt

accounts = []

# ADD ACCOUNT
def add_account():
    acc_no = int(input("Enter Account Number: "))
    name = input("Enter Account Holder Name: ")
    acc_type = input("Enter Account Type (Saving/Current): ")
    balance = float(input("Enter Balance: "))

    account = {
        "acc_no": acc_no,
        "name": name,
        "type": acc_type,
        "balance": balance
    }

    accounts.append(account)
    print("Account Created Successfully!")

# DISPLAY ACCOUNTS
def display_accounts():
    if not accounts:
        print("No accounts found!")
    else:
        for acc in accounts:
            print(acc)

# UPDATE ACCOUNT
def update_account():
    acc_no = int(input("Enter Account Number to update: "))
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            acc["name"] = input("Enter new name: ")
            acc["type"] = input("Enter new type: ")
            acc["balance"] = float(input("Enter new balance: "))
            print("Account Updated!")
            return
    print("Account not found!")

# DELETE ACCOUNT
def delete_account():
    acc_no = int(input("Enter Account Number to delete: "))
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            accounts.remove(acc)
            print("Account Deleted!")
            return
    print("Account not found!")

# CHART: BALANCE DISTRIBUTION
def chart_balance():
    if not accounts:
        print("No data for chart!")
        return

    names = [acc["name"] for acc in accounts]
    balances = [acc["balance"] for acc in accounts]

    plt.pie(balances, labels=names, autopct='%1.1f%%')
    plt.title("Balance Distribution")
    plt.show()

# MENU
while True:
    print("\n--- Banking Management System ---")
    print("1. Add Account")
    print("2. Display Accounts")
    print("3. Update Account")
    print("4. Delete Account")
    print("5. Chart: Balance Distribution")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_account()
    elif choice == 2:
        display_accounts()
    elif choice == 3:
        update_account()
    elif choice == 4:
        delete_account()
    elif choice == 5:
        chart_balance()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
