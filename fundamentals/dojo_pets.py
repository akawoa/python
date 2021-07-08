# class BankAccount:
#     # don't forget to add some default values for these parameters!
#     bank_name = "First Bank of Anime"
#     account_list = []

#     def __init__(self, name, int_rate, balance):
#         # your code here! (remember, instance attributes go here)
#         # don't worry about user info here; we'll involve the User class soon
#         self.name = name
#         self.int_rate = int_rate
#         self.balance = balance
#         BankAccount.account_list.append(self)

#     def deposit(self, amount):
#         self.balance += amount
#         return self

#     def withdraw(self, amount):
#         self.balance -= amount
#         return self

#     def display_account_info(self):
#         print(
#             f"{self.name}'s Account Balance: {self.balance}, Interest Rate: {self.int_rate}")
#         return self

#     def yield_interest(self):
#         self.balance += self.int_rate * self.balance
#         return self

#     def current_balance(self):
#         print(self.balance)
#         return self

# # zerotwo = BankAccount("ZeroTwo", .07, 0)
# # holo = BankAccount("Holo", .25, 0)
# # kyouko = BankAccount("Kyouko Hori", .05, 1337)


# class User:
#     user_list = []

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(name, int_rate=0.02, balance=0)
#         User.user_list.append(self)

#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         return self

#     def make_withdrawal(self, amount):
#         self.account.withdraw(amount)
#         return self

#     def display_user_balance(self):
#         print(self.account.balance)
#         return self


# zerotwo = User("ZeroTwo", "02@python.com")
# print(zerotwo.name)
# print(zerotwo.email)
# print(zerotwo.account.name)
# print(zerotwo.account.int_rate)
# zerotwo.make_deposit(100).display_user_balance()

class Pet:
    pets_list = []
    # implement __init__( name , type , tricks ):

    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 50
        self.energy = 50
        Pet.pets_list.append(self)

    def sleep(self):
        # sleep() - increases the pets energy by 25
        self.energy += 25
        return self

    def eat(self):
        # eat() - increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        # play() - increases the pet's health by 5
        self.health += 5
        return self

    def noise(self):
        # noise() - prints out the pet's sound
        print(self.sound)
        return self


class Ninja:
    ninja_list = []
    # implement __init__( first_name , last_name , treats , pet_food , pet )

    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        Ninja.ninja_list.append(self)
        
    def walk(self):
        # walk() - walks the ninja's pet invoking the pet play() method
        self.pet.energy -= 10
        self.pet.health += 10
        return self

    def feed(self):
        # feed() - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
        return self

    def bathe(self):
        # bathe() - cleans the ninja's pet invoking the pet noise() method
        self.pet.energy += 50
        self.pet.health += 50
        return self


yoko = Ninja("Yoko", "Littner", "salmon", "kibble", Pet("Boota", "mole", "Wears sunglasses", "Reeeeee"))
ammy = Pet("Amaterasu", "God of Nature","Flying and other god stuff", "uwu!!!!")
kyouko = Ninja("Kyouko", "Hori", "steak", "stew", ammy)

print(yoko.first_name)
print(yoko.last_name)
print(yoko.treats)
print(yoko.pet_food)
print(yoko.pet.name)
print(yoko.pet.type)
print(yoko.pet.tricks)
print(yoko.pet.sound)
print(ammy.name)
print(kyouko.first_name)
print(kyouko.last_name)
print(kyouko.treats)
print(kyouko.pet_food)
print(kyouko.pet.name)
print(kyouko.pet.type)
print(kyouko.pet.health)
print(kyouko.pet.energy)
kyouko.pet.noise()
kyouko.walk()
print(kyouko.pet.energy)
kyouko.walk()
print(kyouko.pet.energy)
kyouko.feed()

print(kyouko.pet.energy)
print(kyouko.pet.health)
kyouko.bathe()
print(kyouko.pet.energy)
print(kyouko.pet.health)

# Create a Ninja class with the ninja attributes listed above.

# Create a Pet class with the pet attributes listed above.

# Implement walk(), feed(), bathe() on the ninja class.

# Implement sleep(), eat(), play(), noise() methods on the pet class.

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.

# Have the Ninja feed, walk , and bathe their pet.

# NINJA BONUS: Use modules to separate out the classes into different files.

# SENSEI BONUS: Use Inheritance to create sub classes of pets.

# Compress or zip up assignment and upload it.
