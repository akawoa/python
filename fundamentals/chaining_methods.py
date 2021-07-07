class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    

zerotwo = User("ZeroTwo", "02@python.com")
holo = User("Holo", "Holo@python.com")
kyouko = User("Kyouko Hori", "khori@python.com")

zerotwo.make_deposit(100).make_deposit(100).make_deposit(100)
holo.make_deposit(200).make_deposit(200).make_withdrawal(111).make_withdrawal(111)
kyouko.make_deposit(1000).make_withdrawal(500).make_withdrawal(50).make_withdrawal(27)
zerotwo.make_withdrawal(231).display_user_balance()
holo.display_user_balance()
kyouko.display_user_balance()
