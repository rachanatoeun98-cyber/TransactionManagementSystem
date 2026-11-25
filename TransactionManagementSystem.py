# ======== Transaction Management System ========
class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited Rs. {amount}")
        print("Amount Deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdraw Rs. {amount}")
            print("Withdraw Successful")
        else:
            print("Insufficient Money!")

    #Transfer money
    def transfer(self, reciever, amount):
        if amount <= self.balance:
            self.balance -= amount
            reciever.balance += amount

            self.transactions.append(
                f"Transferred Rs. {amount} to Account {reciever.acc_no}"
            )

            reciever.transactions.append(
                f"Recieved Rs. {amount} to Account {self.acc_no}"
            )
            print("Transfer Successfull")
        else:
            print("Insufficient Balance.")

    # Show Transactions
    def show_transactions(self):
        print("\n ------ Transactions History-------")
        if self.transactions:
            for t in self.transactions:
                print(t)
        else:
                print("No Transaction Found")
        print("-----------------------------------")

    # Display details
    def display(self):
        print(f"{self.acc_no} \t{self.name}\t{self.balance}")

class TransactionManagementSystem:
    def __init__(self):
        self.accounts = []

    # Find Account
    def find_account(self, acc_no):
        for acc in self.accounts:
            if acc_no == acc.acc_no:
                return acc
        return None

    # Create account
    def create_account(self):
        acc_no = int(input("Enter Account No: "))
        name = input("Enter Account Holder Name: ")
        balance = float(input("Enter Balance: "))

        acc = Account(acc_no, name, balance)
        self.accounts.append(acc)

        print("Account Created Successfully!")

    # Deposit
    def deposit_money(self):
        acc_no = int(input("Enter Account No: "))
        acc = self.find_account(acc_no)

        if acc:
            amount = float(input("Enter Amount to deposit: "))
            acc.deposit(amount)
        else:
            print("Account Not Found")    

    # Withdraw Money
    def withdraw_money(self):
        acc_no = int(input("Enter Account No: "))
        acc = self.find_account(acc_no)

        if acc: 
            amount = float(input("Enter Amount to Withdraw: "))
            acc.withdraw(amount)
        else:
            print("Account Not Found")

    # Transfer Money
    def transfer_money(self):
        sender_no = int(input("Enter sender Account No: "))
        reciever_no = int(input("Enter Reciever Account No: "))

        sender = self.find_account(sender_no)
        reciever = self.find_account(reciever_no)

        if sender and reciever:
            amount = float(input("Enter Transfer Money: "))
            sender.transfer(reciever, amount)
        else:
            print("Invalid Account Number!")

    # Transaction History
    def transaction_history(self):
        acc_no = int(input("Enter Account number: "))
        acc = self.find_account(acc_no)

        if acc:
            acc.show_transactions()
        else:
            print("Account Not Found")

    # Check Balance:
    def check_balance(self):
        acc_no = int(input("Enter Account No: "))
        acc = self.find_account(acc_no)

        if acc:
            print(f"Current Balance Rs. {acc.balance}")
        else:
            print("Account Not Found")

    # Display All Account
    def display_all(self):
        print("\nAcc_no\tName\tBalance")
        print("---------------------------")
        for acc in self.accounts:
            acc.display()

    # ---------Main Program--------------
system = TransactionManagementSystem()

while True:
    print("\n ===========Transaction Management System====================")
    print("1. Create Account")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transaction History")
    print("6. Check Balance")
    print("7. Display All Accounts")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))
# Showing up choice after user input
    if choice == 1:
        system.create_account()
    elif choice == 2:
        system.deposit_money()
    elif choice == 3:
        system.withdraw_money()
    elif choice == 4:
        system.transfer_money()
    elif choice == 5:
        system.transaction_history()
    elif choice == 6:
        system.check_balance()
    elif choice == 7:
        system.display_all()
    elif choice == 8:
        print("System Closed!")
        break
    else:
        print("Invalid Choice.")
