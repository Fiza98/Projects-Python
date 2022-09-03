#Question 1

#Write a program to perform as mini calculator. 
#The following are the requirements:
#Input: a) arithmetic symbol ‘+’ for addition, ‘-‘ for subtraction, ‘*’ for multiplication and ‘/’ for division.
#       b) two numbers
#output: the result of the calculation based on the arithmetic symbol entered by user.

symbol = input("Enter an arithmetic symbol (+,-,*,/) : ")
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if (symbol == '+'):
    result = n1 + n2
elif (symbol == '-'):
    result = n1 - n2
elif (symbol == '*'):
    result = n1 * n2
elif (symbol == '/'):
    result = n1 / n2           #assuming n2 is not 0
else:
    result = 0
    print("wrong arithmetic symbol!!!")
    
print(n1, ' ',symbol,' ',n2, ' = ',result)



#Question 2

#Write a program, which will imitate an ATM machine. 
#The program will ask for a password. Assume that only password “abcde” is accepted. If the password is correct, display the following menu.
#Menu ATM Bank
#1. Balance Inquiry
#2. Deposit
#3. Withdrawal
#4. Transfer fund
#0. Exit
#Your choice: ______
#Option 1 will display the current balance. Assume all customers will have an initial balance of RM1000.00.
#Option 2 will input an amount and add the amount to the current balance.
#Option 3 will input an amount and deduct the amount from the current balance.
#Option 4 will input an account number (numbers) and amount to transfer, and it will deduct the amount from the current balance. The following message will be displayed.
#<amount transfer> has been transferred to account no <account number>.
#The program will continue until user chooses 0 to exit.

pwd = input("enter your password: ")
choice = 1
balance = 1000
if (pwd == 'abcde'):
    while (choice != 0):
        print("Menu ATM BAnk")
        print("1. Balance Inquiry")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Transfer fund")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            print("Your balance is RM",balance)
            print()
        elif (choice == 2):
            dep = int(input("Enter the deposit amount RM"))
            balance = balance + dep
            print("Your balance now is RM",balance) 
           
        elif (choice == 3):
            wtd = int(input("Enter the withdrawal amount RM"))
            balance = balance - wtd
            print("Your balance now is RM",balance)
            print()
            print()
        elif (choice == 4):
            acctno = input("Enter the account number to transfer to: ")
            amt = int(input("Enter the amount to transfer RM"))
            balance = balance - amt
            print(amt, " has been transferred to account no ",acctno)
            print("Your balance now is RM",balance)
            print()
            print()
        elif (choice == 0):
            print("You are exiting the ATM Menu")
        else:
            print("You have chosen the wrong choice!!!")
            print("Please enter the correct choice again")
            print()

print("Thank you for using ATM")
