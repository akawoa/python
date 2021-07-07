class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    

zerotwo = User("ZeroTwo", "02@python.com")
holo = User("Holo", "Holo@python.com")
kyouko = User("Kyouko Hori", "khori@python.com")

zerotwo.make_deposit(100)
zerotwo.make_deposit(100)
zerotwo.make_deposit(100)
holo.make_deposit(200)
holo.make_deposit(200)
holo.make_withdrawal(111)
holo.make_withdrawal(111)
kyouko.make_deposit(1000)
kyouko.make_withdrawal(500)
kyouko.make_withdrawal(50)
kyouko.make_withdrawal(27)
zerotwo.make_withdrawal(231)
zerotwo.display_user_balance()
holo.display_user_balance()
kyouko.display_user_balance()
