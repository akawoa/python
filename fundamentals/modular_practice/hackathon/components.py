import random
game_over = False
# Completed Project with Kara, Itai, and Li-Yen 
generic_attacks = {  
    "laser" : {"damage":250, "hitRate": 10},
    "bomb" : {"damage": 100, "hitRate": 6},
    "missile": {"damage": 70, "hitRate": 8}
    }

class Ship:
    
    def __init__(self, name, health = 500, attacks = generic_attacks):
        self.name = name
        self.health = health
        self.attacks = attacks
    
# ------ --------------   
#need to add target and functionality to decrease health
    def dies(self):
        print(f"{self.name} died!")

    def takes_damage(self, damage_done):
        self.health -= damage_done
        if self.health <= 0:
            self.dies()

    def attack(self, attackUsed, target_ship): 
        if (willAttackLand(attackUsed) == True):
            print("An attack was used!")
            damage_done = self.attacks[attackUsed]["damage"]
            # if self. type is player and (target_ship is an  "alien", see if  Alien blocks the attack...
            if (isinstance (self, Player) and isinstance(target_ship, Alien)):
                if  target_ship.block_result() == True:
                    print("The alien has blocked your attack")
                    # if the alien blocks the attack, alert that the alien blocked the attack 
                else:
                    print("The alien was hurt!")
                    target_ship.takes_damage(damage_done)
                    #target_ship.
            # otherwise if player attacked  alien and the block failed what do we do... subtract the attack damage from the target ships health 
            elif (isinstance (self, Alien) and isinstance(target_ship, Player)):
        # if self. type is alien and target_ship is an  "player", since we dont have block at the player we take the damage
                target_ship.takes_damage(damage_done)
            # if attack used's damage brings the player to 0 or below health, see if we have any regenerations i.e., see if we have any lives left
                # set the players health to 500 and decrease player life by 1
                #  if no lives left print to user game over  
        else:
            print("Attack missed!")

class Player(Ship):
    def __init__(self, name, health = 500, attacks = generic_attacks, lives = 3):
        super().__init__(name, health, attacks)
        self.lives = lives

    def takes_damage(self, damage_done):
        super().takes_damage(damage_done)
        global game_over
        if self.health <= 0:
            if self.lives == 0:
                self.dies()
                print("Game Over!")
                game_over = True

            else:
                self.lives -= 1
                self.health = 500
                print(f"Player ship regenerated, lives left:{self.lives}")

class Alien(Ship):
    all_aliens = []
    def __init__(self, name, health = 400, attacks = generic_attacks, blockChance = 1):
        super().__init__(name, health, attacks)
        self.blockChance = blockChance
    
    def block_result(self):
        randomNumber = random.randint(1,10)
        if randomNumber == self.blockChance:
            print("The attack has been blocked")
            return True

        else:
            print("Block was failed!")
            return False

    def dies(self):
        global game_over
        super().dies()
        game_over = True

        


#-- not part of any class
def willAttackLand(attackUsed):
    randomNumber = random.randint(1,10)
    mustBeBelow = generic_attacks[attackUsed]["hitRate"]
    if(randomNumber > mustBeBelow):
        return False
    else:
        return True

#TESTING AREA
print("Let's play!")
player_name = input("Name your ship:")
playerShip = Player(player_name)

alienShip = Alien("Alien1") # SO right now this instance of the Alien object is named Alien1, health is 400 attacks is the list of generic attakcs and 10% block capabilites



# alien attacks

def playerMove():
    print("Player's turn")
    attackUsed = input("Please enter one of the following values:\n laser\n bomb\n missile\n").lower()
    playerShip.attack(attackUsed,alienShip) 

def alienMove():
    print("Alien's turn")
    attacks = ["laser", "missile", "bomb"]
    attackChoice = random.randint(0,2)
    # print(f"attchChoice: {attackChoice}")
    alienShip.attack(attacks[attackChoice],playerShip)

# player will attack as long as game is not over
while game_over == False:
    playerMove()
    if game_over == False:
        alienMove()
    # else:
    #     break

print("[̲̅g][̲̅a][̲̅m][̲̅e] [̲̅o][̲̅v][̲̅e][̲̅r]")




#playerShip.attack("bomb") #does miss eventually
#future idea: menu to take input
