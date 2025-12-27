# Parent class 
class account:
    def __init__(self,acno,acname,curbalance,mobile,minibalance):
        self.acno=acno
        self.acname=acname
        self.curbalance=curbalance
        self.mobile=mobile
        self.minibalance=minibalance
    def deposit(self,amount):
        self.curbalance+=amount
        print(f'₹ {amount}is deposited . Nem balance is {self.curbalance}₹')
    def withdrawl(self,amount):
        if self.curbalance - amount >= self.minibalance:
            self.curbalance-=amount
            print(f'₹ {amount}is withdrawl form the accont . New balance is {self.curbalance}₹')
        else:
            print(' Insufficient balance to withdrawl')
    def print_detail(self):
        print(f'Accont no is {self.acno}')
        print(f'Account name is {self.acname}')
        print(f'The current balance in the account is {self.curbalance} ₹')
        print(f'Mobile no of account holder is {self.mobile}')
        print(f'The minimum balance fix by you is {self.minibalance} ₹')

# Child class of Account parent class.
class saving(account):
    def __init__(self, acno, acname, curbalance, mobile, minibalance):
        super().__init__(acno, acname, curbalance, mobile, minibalance)
        self.checkbook=False
    def calinterest(self):
        self.interest = self.curbalance*0.04
        print(f'interest eraned {self.interest}')

# Another child class of Account parent class.
class current(account):
    def __init__(self, acno, acname, curbalance, mobile, minibalance):
        super().__init__(acno, acname, curbalance, mobile, minibalance)
        self.checkbook=True
    def calinterest(self):
        self.interest = self.curbalance*0.02
        print(f'interest eraned {self.interest}')

# while loop for getting continous output.
# Or display like a menu driven program.     
#  
account = None
while True:
    print("\nAccount Menu:")
    print("1. Create Savings Account")
    print("2. Create Current Account")
    print("3. Exit")
    choice = input("Your Choice (1-3): ")
    if choice == '1' or choice == '2':
        acno = int(input("Enter Account No: "))
        acname = input("Enter Customer Name: ")
        curbalance = float(input("Enter Current Balance: "))
        mobile = int(input("Enter Mobile No: "))
        minibalance = float(input("Enter Minimum Balance: "))

        if choice == '1':
            account = saving(acno, acname, curbalance, mobile, minibalance)
        else:
            account = current(acno, acname, curbalance, mobile, minibalance)

        while True:
            print("\nTransaction Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Print Account Details")
            print("4. Calculate Interest")
            print("5. Back to Account Menu")
            t_choice = input("Your Choice (1-5): ")

            if t_choice == '1':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif t_choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdrawl(amount)
            elif t_choice == '3':
                account.print_detail()
            elif t_choice == '4':
                account.calinterest()
            elif t_choice == '5':
                break
            else:
                print("Invalid transaction choice.")
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid account choice.")

