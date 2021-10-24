# Name: Ayman Almansor
# Description: This program automate an Automatic Teller Machine(ATM)

class BankAccount:

    # Constructor
    def __init__(self):
        # Private class attributes
        self.__balance = 1000.00
        self.__transCount = 0
        self.__history = []  # Holds transactions type plus amount

    # Deposit method
    def deposit(self, amount):
        self.__balance += amount
        self.__history.append(["Deposit", format(amount, ",.2f")])  # Saves the transaction history
        print("[+] Deposit complete")
        self.__transCount += 1  # Track transactions completed

    # Withdrawal method
    def withdraw(self, amount):
        if amount % 10 == 0  and amount != 0:  # Checks if withdrawal is in denomination of $10
            if self.__balance >= amount:  # Checks if funds are sufficient
                self.__balance -= amount  # If sufficient extract the amount from the balance
                print("[+] Withdrawal complete")
                self.__history.append(["Withdrawal", format(-amount, ",.2f")])
                self.__transCount += 1
            else:
                self.__history.append(["Failed Withdrawal", format(amount, ",.2f")])
                print("[!] Error: Insufficient Funds\n"
                      "[!] Your balance is $", format(self.__balance, ",.2f"), sep="")
        else:
            self.__history.append(["Failed Withdrawal", format(amount, ",.2f")])
            print("[!] Error: Withdrawal amount must be in denominations of $10")

    # Balance inquiry
    def getBalance(self):
        print("[+] Account balance: $" + format(self.__balance, ",.2f"))
        self.__history.append(["Balance Check", format(self.__balance, ",.2f")])
        self.__transCount += 1

    # Transactions history method
    def numOfTrans(self):
        print("[+] Transactions Completed: ", self.__transCount)
        print("\nDescription", "\t" * 3, "Amount")
        print("=" * 45)
        # Displays a formatted table for transactions history
        for i in range(len(self.__history)):
            print(self.__history[i][0], " "*(19 - len(self.__history[i][0])), "\t\t", self.__history[i][1] + "$")
        input("\n> Press Enter to continue:")


def menu():  # Menu function
    print("""
[1] Balance Inquiry
[2] Make a Deposit
[3] Make a Withdrawal
[4] Display Number of Transactions
[5] Exit
    """)


def inputChecker():  # Input checker - checks if input is valid
    while True:  # While loop until user enters a valid amount
        try:
            user_input = float(input("> Enter amount: "))
            if user_input > 1:
                return user_input  # Returns the amount if valid
            else:
                print("[!] Please enter a valid number")
        except ValueError:
            print("[!] Please enter a valid number")


def main():  # Main function

    checking = BankAccount()  # Class object

    counter = True
    while counter:
        print("=" * 50)
        menu()  # Displays the menu
        user_choice = input("> Choice: ")  # Takes user choice
        if user_choice == "1":
            checking.getBalance()  # Balance Inquiry
        elif user_choice == "2":
            checking.deposit(inputChecker())  # Make a Deposit
        elif user_choice == "3":
            checking.withdraw(inputChecker())  # Make a Withdrawal
        elif user_choice == "4":
            checking.numOfTrans()  # Display Number of Transactions
        elif user_choice == "5":
            print("\n[+] Thank you for using our service!")
            counter = False  # End the while loop
        else:
            # Displays error message if user choice unavailable option
            print("[!] Please choose an option 1 through 5 only")


main()  # Call main function
