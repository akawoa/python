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
    def current_balance(self):
        print(self.balance)
        return self

# zerotwo = BankAccount("ZeroTwo", .07, 0)
# holo = BankAccount("Holo", .25, 0)
# kyouko = BankAccount("Kyouko Hori", .05, 1337)

class User:
    user_list = []
    def __init__(self, name, email):
        self.name = name
        self.email = email        
        self.account = BankAccount(name, int_rate=0.02, balance=0)	
        User.user_list.append(self)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self):
        print(self.account.balance)
        return self

zerotwo = User("ZeroTwo", "02@python.com")
print(zerotwo.name)
print(zerotwo.email)
print(zerotwo.account.name)
print(zerotwo.account.int_rate)
zerotwo.make_deposit(100).display_user_balance()
