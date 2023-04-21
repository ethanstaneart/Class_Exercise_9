# First Class: BankAccount
class BankAccount:
    def __init__(self, bal):  # The self is used to represent the instance of the class.
        self.balance = bal

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Error: Insufficient funds")

    def get_balance(self):
        return self.balance


# Second Class
def main():
    start_bal = float(input("Enter the starting balance: "))
    savings = BankAccount(start_bal)

    pay = float(input("How much were you paid this week? "))
    print("Will deposit that amount into your account")
    savings.deposit(pay)
    print("Your account balance is $", format(savings.get_balance(), '.2f'))

    cash = float(input("How much would you like to withdraw? "))
    print("Will withdraw that amount from your account")
    savings.withdraw(cash)
    print("Your account balance is $", format(savings.get_balance(), '.2f'))


main()
