import ClientsApp as C

class User:
    def __init__(self, name='', MobileNo='', initalAmount=0, PIN='', AccountNo=0, PaymentAdress='', counter=0):
        # Initialize a User object with the provided parameters
        self.name = name
        self.MobileNo = MobileNo
        self.initalAmount = initalAmount
        self.PIN = PIN
        self.AccountNo = AccountNo
        self.PaymentAdress = PaymentAdress
        self.counter = counter

class Bank:
    def __init__(self):
        # Initialize a Bank object with an empty list of users and placeholder users for the current and receiving users
        self.users = []
        self.CurrentUser = User()
        self.ReceivingUser = User()

    def create_user(self, name, MobileNo, initalAmount, PIN, AccountNo, paymentAdress, counter=0):
        # Create a new user and add them to the users list
        user = User(name, MobileNo, initalAmount, PIN, AccountNo, paymentAdress, counter)
        self.users.append(user)
        return user

    def AccountLogin(self, Account):
        # Log in the user based on their account number
        for user in self.users:
            if user.AccountNo == Account:
                print('Welcome MR:', user.name, '\n')
                print('Please enter your secret pin')
                pin = input()  # Prompt user for PIN
                for i in range(3):  # Allow up to 3 attempts
                    if user.PIN == pin:
                        self.CurrentUser = user
                        return True
                    else:
                        print('Invalid Pin, Try Again')
                        pin = input()
                print('Maximum number of trials exceeded, Logging out \n')
                return False

        print('Account Not found\n')

    def status(self):
        # Display the current user's account status
        print(f'User: {self.CurrentUser.name} \t AccountNo: {self.CurrentUser.AccountNo} \t Balance: {self.CurrentUser.initalAmount} EGP')
        return self.CurrentUser

    def transfer(self, RecPaymentAdress, amount):
        # Transfer money from the current user to another user
        if self.CurrentUser.initalAmount <= amount + 500:  # Check if account balance is sufficient
            print('Cannot Proceed \n Amount unavailable in your account')
        else:
            for user in self.users:
                if user.PaymentAdress == RecPaymentAdress:
                    self.ReceivingUser = user
                    if self.CurrentUser.PaymentAdress == RecPaymentAdress:
                        print('Cannot Transfer money to your own account\n')
                        return
                    else:
                        print('Enter your secret pin to confirm Transaction request:\t')
                        pcode = input()  # Prompt for PIN to confirm transaction
                        if pcode == self.CurrentUser.PIN:
                            self.CurrentUser.initalAmount -= amount
                            self.ReceivingUser.initalAmount += amount
                            print('Transfer Complete')
                            C.UsersData(self.CurrentUser)  # Update user data
                            self.CurrentUser.counter += 1
                            C.Transactioncounter(self.CurrentUser, 'Transferred', amount)  # Log transaction
                            C.UsersData(self.ReceivingUser)  # Update receiving user data
                            self.ReceivingUser.counter += 1
                            C.Transactioncounter(self.ReceivingUser, 'Received', amount)  # Log transaction
                            self.status()  # Display updated status
                            return
                        else:
                            print('Transfer failed')
                            return

            print('Provided payment address is invalid \n')

    def UsersCount(self):
        # Return the count of users in the bank
        count = len(self.users)
        return count

# Create an instance of the Bank class
AmitBank = Bank()
