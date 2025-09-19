import json
import os
if os.path.exists("bank.json"):
    with open("bank.json" , "r")as f:
        account = json.load(f)
else:
    account = {"balance": 0}

while True:
    print("\n--- Banking System ---")
    print("1. View balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is ₹{account['balance']}")
    
    elif choice == 2:
        deposit = int(input("Enter the amount you want to deposit: "))
        account['balance'] += deposit
        with open("bank.json", "w") as f:
            json.dump(account, f, indent=4)
        print(f"${deposit} amount is added to your balance")
    
    elif choice == 3:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw  <= account["balance"]:
            account['balance'] -= withdraw
            with open("bank.json", "w") as f:
                json.dump(account, f, indent=4)
            print(f"your withdraw ${withdraw} from your balance ")
        else:
            print("Insufficiant amount")
    
    elif choice == 4:
        print("Exicting....")
        break
    
    else:
        print("Invalid option.")