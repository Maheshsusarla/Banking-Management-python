import datetime
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time:", current_time)

balance=0.0
transactions=[]

def deposit(amount):
    global balance
    balance+=amount
    transactions.append(f"Deposited{amount}/-\n")
    print(f"{amount} Deposited sucessfully ")


def withdraw(amount):
    global balance
    if amount>balance:
        print("Insufficent balance")
    else:
        balance -=amount
        transactions.append(f"withdrawn{amount}/-")
        print(f"{amount} withdraw sucessfully\n")

def checkBalance():
    print(f"Current Balance{balance}\n")

def transactionhistory():
    if not transactions:
        print("No Transactions yet.\n")
    else:
        print("---Transactions history---")
        for t in transactions:
            print('_',t)
        deposite=sum(1 for t in transactions if 'Deposited' in t)
        withdraws=sum(1 for t in transactions if 'withdrawn' in t)

        print(f"\n Total Deposites:{deposite}")
        print(f"\n Total Deposites:{withdraws}")

def menu():
    while True:
        print("-----Python Banking menu-----")
        print("1. Deposite")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Viwe transaction history")
        print("5. Exit")

        choice=input("Enter your opction:")

        if choice =="1":
            amount=float(input("Enter your amount to deposit"))
            deposit(amount)
        elif choice =="2":
            amount=float(input("Enter your amount to deposit"))
            withdraw(amount)
        elif choice =="3":
            checkBalance()
        elif choice =="4":
            transactionhistory()
        elif choice =="5":
            print("Thankyou you for using python banking")
            break
        else:
            print("Invalid Option")
menu()