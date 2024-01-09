import time
import random

def get_account_number():
    while True:
        account_no = int(input("\nEnter your card number: \n"))
        if 10000000 <= account_no <= 99999999:
            return account_no
        else:
            print("Account number should be of 8 numbers :) \n\n")

def withdraw_money(balance):
    while True:
        money = float(input("\nEnter the money you want to withdraw  ₹"))
        if money > balance:
            time.sleep(1)
            print("\nYour balance is lower than the amount you want to withdraw")
        elif money < 100:
            print("Minimal amount should be ₹100")
        else:
            return money

def deposit_money(balance):
    money = float(input("\nEnter the amount you want to deposit  ₹"))
    return balance + money

def transfer_money(balance, account_no):
    while True:
        money = float(input("\nEnter the amount you want to transfer : ₹"))
        ac = float(input("\nEnter the account you want to transfer to "))
        if ac == account_no:
            print("\nCan't send money to yourself, can you? \n")
        elif not (10000000 <= ac < 99999999):
            print("\nAccount no. should be of 8 digits\n")
        elif money > balance or money < 100:
            if money > balance:
                print("Not enough money in your account \n")
            else:
                print("Minimal transfer amount is ₹100\n")
        else:
            time.sleep(2)
            balance -= money
            print(f"\nTransferred amount  ₹{money:.3f} To Account with account no: {int(ac)}\n")
            print(f"Your bank now has ₹{balance:.3f}")
            return balance


c = random.randint(1000, 10000)
account_no = get_account_number()

print("\n\nChecking your card status please wait :) \n")
time.sleep(2)
print("\nWELCOME TO ATM ")

while True:
    print("\n\nWhat would you like to do?\n1. Withdrawal\n2. Check balance\n3. Deposit money\n4. Transfer money \n5. Cancel \n")
    n = int(input())
    
    if n == 1:
        c -= withdraw_money(c)
        time.sleep(2)
    elif n == 2:
        print(f"\nYour account has ₹{c:.3f}\n")
    elif n == 3:
        c = deposit_money(c)
        print("Successfully deposited ")
        
    elif n == 4:
        c = transfer_money(c, account_no)
    elif n == 5:
        print("\nTHANK YOU FOR CHOOSING US :) \n\n")
        break
    else:
        print("\nInvalid option :)\n")