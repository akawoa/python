# As we continue thinking about our banking application, we realize that it would be more accurate to assign a balance not to the user directly, but that in the real world, users have accounts, and accounts have balances. This gives us the idea that maybe an account is its own class! But as we stated, it is not completely independent of a class; accounts only exist because users open them.

# For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!

# Let's first just get some more practice writing classes by writing a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like this:

class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "First Bank of Anime"
    account_list = []
    def __init__(self, name, int_rate, balance): 
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_list.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"{self.name}'s Account Balance: {self.balance}, Interest Rate: {self.int_rate}")
        return self
    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self

zerotwo = BankAccount("ZeroTwo", .07, 0)
holo = BankAccount("Holo", .25, 0)
kyouko = BankAccount("Kyouko Hori", .05, 1337)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

zerotwo.deposit(100).deposit(100).deposit(100).withdraw(231).yield_interest().display_account_info()
holo.deposit(100).deposit(100).withdraw(25).withdraw(25).withdraw(50).withdraw(77).yield_interest().display_account_info()
kyouko.display_account_info()

# class BankAccount:
#     # class attribute
#     bank_name = "First National Dojo"
#     all_accounts = []
#     def __init__(self, int_rate,balance):
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.all_accounts.append(self)
#     
#     # class method to change the name of the bank
#     @classmethod
#     def change_bank_name(cls,name):
#         cls.bank_name = name
#     # class method to get balance of all accounts
#     @classmethod
#     def all_balances(cls):
#         sum = 0
#         # we use cls to refer to the class
#         for account in cls.all_accounts:
#             sum += account.balance
#         return sum
