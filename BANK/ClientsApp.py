import os
import shutil
from BankServer import AmitBank

# Directory where customer data will be stored
directory = '.\\Bank Customers'

# Remove the existing directory if it exists
if os.path.exists(directory):
    shutil.rmtree(directory)

# Create a new directory for storing customer data
os.mkdir(directory)

def Numbering():
    # Function to get integer input from the user
    num = int(input())
    return num

def UsersData(obj):
    # Function to save user data to a file
    path = os.path.join(directory, obj.name)
    if not os.path.exists(path):
        os.mkdir(path)  # Create directory for the user if it does not exist
    NewDir = path + '\\Info.txt'
    with open(NewDir, 'w') as file:
        file.write(f'Name: {obj.name}\nMobile Number: {obj.MobileNo}\nBalance: {obj.initalAmount}\nAccount Number: {obj.AccountNo}\nPayment Address: {obj.PaymentAdress}\n')

def Transactioncounter(obj, type, amount):
    # Function to log transactions to a file
    path = os.path.join(directory, obj.name)
    if not os.path.exists(path):
        os.mkdir(path)  # Create directory for the user if it does not exist
    NewDir = path + '\\Transactions.txt'
    with open(NewDir, 'a+') as file:
        file.write(f'-Transaction number {obj.counter}:\t{type}\t\t{amount}\t\n\n')

def AccountMenu():
    # Function to display account menu and handle account operations
    u1 = AmitBank.status()  # Get the current status of the account
    print('Press 1 for Deposit:\nPress 2 for Withdrawal: \nPress 3 for money transfer:\nPress 4 to log out\n')
    AccountInp = Numbering()  # Get user input for menu options

    # Validate user input
    while AccountInp <= 0 or AccountInp > 4:
        print("Invalid Input\t Please Try again\n")
        print('Press 1 for Deposit:\nPress 2 for Withdrawal: \nPress 3 for money transfer:\nPress 4 to log out\n')
        AccountInp = Numbering()

    while AccountInp != 4:  # Continue until the user chooses to log out
        AmitBank.status()  # Display current account status

        ################ DEPOSITING MONEY ##################
        if AccountInp == 1:
            print('Enter your deposited amount\n')
            DepositAmount = Numbering()  # Get deposit amount
            u1.initalAmount += DepositAmount  # Update account balance
            print(f'New Balance: {u1.initalAmount}')
            UsersData(u1)  # Save updated user data
            u1.counter += 1  # Increment transaction counter
            Transactioncounter(u1, 'Deposit', DepositAmount)  # Log transaction
            print('Press 1 for Deposit:\nPress 2 for Withdrawal: \nPress 3 for money transfer:\nPress 4 to log out\n')
            AccountInp = Numbering()  # Get new user input

        ################ WITHDRAWING MONEY ##################
        elif AccountInp == 2:
            print('Enter Amount to Withdraw\n')
            WithdrawAmount = Numbering()  # Get withdrawal amount
            if u1.initalAmount < WithdrawAmount:
                print('Amount is not available in your account\n')
                print(f'Your current balance is: {u1.initalAmount}')
                print('Press 1 for Deposit:\nPress 2 for Withdrawal: \nPress 3 for money transfer:\nPress 4 to log out\n')
                AccountInp = Numbering()  # Get new user input
            else:
                print('Transaction processing\n')
                u1.initalAmount -= WithdrawAmount  # Update account balance
                print(f'Your new balance is: {u1.initalAmount}')
                UsersData(u1)  # Save updated user data
                u1.counter += 1  # Increment transaction counter
                Transactioncounter(u1, 'Withdrawal', WithdrawAmount)  # Log transaction
                print('Press 1 for Deposit:\nPress 2 for Withdrawal: \nPress 3 for money transfer:\nPress 4 to log out\n')
                AccountInp = Numbering()  # Get new user input

        ################ TRANSFERRING MONEY ##################
        else:
            RecpAdress = input('Please Enter the recipient payment address\n')
            bankadress = '@AmitBank'
            RecpPaymentAdress = RecpAdress + bankadress  # Construct recipient payment address
            print('Enter Transferred amount\n')
            TransAmount = Numbering()  # Get transfer amount
            AmitBank.transfer(RecpPaymentAdress, TransAmount)  # Perform money transfer
            print('Press 1 for Deposit:\nPress 2 for Withdrawal: \nPress 3 for money transfer:\nPress 4 to log out\n')
            AccountInp = Numbering()  # Get new user input

    print('\n Logging Out\n')
    return
