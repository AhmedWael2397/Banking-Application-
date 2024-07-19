import ClientsApp as C
import BankServer as B
import random

# Function to display the main menu and get user input
def MainMenu():
    # Display menu options
    print('Press 1 for creating a new customer:\nPress 2 for logging in as an existing customer: \nPress 3 for displaying number of customers:\nPress 4 for exit\n')
    # Get user input
    user_input = C.Numbering()
    # Validate user input
    while user_input <= 0 or user_input > 4:
        print("Invalid Input\t Please Try again\n")
        print('Press 1 for creating a new customer:\nPress 2 for logging in as an existing customer: \nPress 3 for displaying number of customers:\nPress 4 for exit\n')
        user_input = C.Numbering()
    return user_input

# Main loop to keep the program running
while True:
    # Get user input from the main menu
    UserInput = MainMenu()

    # If user selects 1, create a new customer
    if UserInput == 1:
        name = input('Please Enter your Name\n')
        phone = input('Please Enter your Mobile Number\n')
        print('Please Enter the amount that you will deposit')
        Deposit = C.Numbering()
        # Validate deposit amount
        while Deposit < 500 or Deposit <= 0:
            print('Sorry but minimum Amount to open an account is 500 EGP\n')
            Deposit = C.Numbering()
        # Get and validate pin code
        print('Please Enter your desired Pin-Code')
        NewCode = input()
        while len(NewCode) != 4:
            print('Sorry but PinCode must be 4 characters\n')
            NewCode = input()
        # Generate a random account number
        AccountNo = random.randint(100000, 500000)
        Adress = input('Please Enter your desired payment address\n')
        PaymentAdress = Adress + '@AmitBank'
        counter = 0
        # Create a new user
        u2 = B.AmitBank.create_user(
            name, phone, Deposit, NewCode, AccountNo, PaymentAdress, counter)
        # Save user data
        C.UsersData(u2)
        # Confirm account creation
        print('User Account Created successfully\n Welcome to Amit Bank Mr: ',
              u2.name, '\n Your Account number is: ', u2.AccountNo, 'your payment address is ', u2.PaymentAdress)

    # If user selects 2, log in as an existing customer
    elif UserInput == 2:
        print('Please Enter your Account Number: ')
        UserAccount = C.Numbering()
        # Check if login is successful
        if B.AmitBank.AccountLogin(UserAccount):
            print('Logged in \n')
            SecondInput = C.AccountMenu()
        else:
            print('Login Failed')

    # If user selects 3, display the number of customers
    elif UserInput == 3:
        UC = B.AmitBank.UsersCount()
        print(f'Number of Users in Amit Bank is: {UC} Users')

    # If user selects 4, exit the program
    elif UserInput == 4:
        print("Exiting...")
        break
