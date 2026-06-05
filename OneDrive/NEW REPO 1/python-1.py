# #                                   ~BANK MANAGEMENT SYSTEM~

# vcgfctyhg

# INTRO PAGE

class Bank:
    balance = 1000


# # STAGE~1  CREATE A NEW ACCOUNT

class New_account:
    def new_account(self):
        print()
        print("                                     ~Welcome to Apna-Bank~                                               ")
        print()
        print("\nCreate a New Account")
        print()
        self.name=input("Enter your Name:")
        self.age=int(input("Enter your Age :"))
        self.gender=input("Enter your Gender:")
        self.username=input("Create your Username:")
        self.ATM=int(input("Create your ATM Number :"))
        self.PIN=int(input("Create your PIN:"))
        print("\nYour Account Create in Successfully ")
        print()
        print("~Thank you for visiting have a good day~\n")

#
# #       STAGE ~ 2
#
# #       REGISTRATION PAGE~
class Registration:
    def registration(self):
        print()
        print("\nHello Welcome to Registration page: ")
        print()

        self.ATM=int(input("Enter your ATM Number :"))
        self.PIN=int(input("Enter your PIN:"))
        if self.ATM!=self.PIN:
            print()
            print("\n~Your Registration is successful~ ")
        else:
            print()
            print("~Wrong PIN, Please try again~")
            print()
        print("~Thankyou for visiting, have a good day~\n")
        print()

#
# #STAGE~3       USER WITHDRAWAL

class Withdrawal:
    def withdrawal(self):
        print("\n~Hello Welcome to the withdrawal page~")
        print()
        print("ATM CARD + PIN (only if they trust you):")
        print()
        self.ATM=int(input("Enter your ATM Number :"))
        self.PIN=int(input("Enter your PIN:"))
        print()
        amount = int(input("Enter Withdrawal Amount:"))
        if amount<=Bank.balance:
            Bank.balance-=amount

            print("Withdrawal Successful")
            print("Remaining Balance:",Bank.balance)
        else:
            print("Insufficient Balance")


#
# #STAGE~4

# ADD AND DEPOSIT MONEY ~

class Deposit_Money:
    def deposit_money(self):
        print("\n~Welcome to cash deposit money machine~")
        print()
        print("~ Deposit using a cash deposit machine(CDM)")
        print()
        self.ATM=int(input("Enter your account number if supported:"))
        print()
        amount = int(input("Insert your cash: "))
        Bank.balance+=amount
        print("Deposit Successful")
        print("Current Balance:",Bank.balance)


#
# #STAGE~5
# #           CHECK BALANCE

class Check:
    def check(self):
        print("\n~Welcome to the check-balance page~")
        print()


        print("\n your current balance is:",Bank.balance)
        print()
        print("~Thankyou for visiting , have a good day~\n")



class Intro:
    def __init__(self):

       #        INTRO

        print("      WELCOME TO APNA BANK")


        print("1. Create New Account")
        print("2. Registration")
        print("3. Deposit Money")
        print("4. Withdrawal")
        print("5. Check Balance")
        print("6. Exit")

        choice = int(input("\nChoose Operation: "))

        if choice == 1:
            pass


            # obj = New_account()
            # obj.new_account()


        elif choice == 2:
            obj = Registration()
            obj.registration()


        elif choice == 3:
            Deposit_Money.deposit_money()

        elif choice == 4:
            Withdrawal().withdrawal()

        elif choice == 5:
            Check().check()

        elif choice == 6:
            print("Thank you for using Apna Bank.")

        else:
            print("Invalid Choice!")


# PROGRAM STARTS HERE
Intro()