import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, heals_left, special1, special2):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health # Store the original health for maximum limit
        self.heals_left = heals_left  ## Store Heals left for each character
        self.special1 = special1 ## Special abilities
        self.special2 = special2

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    ##Create choice for special ability
    def special_attack(self, opponent):
        while True:
            print('\n --- Choose Special Ability to use ---')
            print(f'1. {self.special1.__name__.replace("_", " ").title()}') ##Title of function but replacing _ and capitalizing with .title()
            print(f'2. {self.special2.__name__.replace("_", " ").title()}')
            choice = input('Choose an action: ')
            if choice == '1':
                self.special1(opponent)
                break
            elif choice == '2':
                self.special2(opponent)
                break
            else:
                print("Invalid choice, try again.")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Heal Method
    def heal(self):

        if self.heals_left > 0:
            self.health += 20
            self.heals_left -= 1 ##Subtract one heal from total available heals
            if self.health > self.max_health:
               self.health = self.max_health ##Only Regen to max health
            print(f"{self.name} \nregenerates 20 health! Current health: {self.health} \nHeals left: {self.heals_left}")
        else:
            print(f"{self.name} \nhas no heals left!")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=40, heals_left=3, special1=self.power_ax, special2=self.defensive_stance) 

    ##Specials
    def power_ax(self, opponent):
        damage = 65
        opponent.health -= damage
        print(f"{self.name} uses Power Ax! Deals {damage} damage.")

    # Function Does not work at the moment
    def defensive_stance(self, opponent):
        print(f"{self.name} uses Defensive Stance! Reduces damage taken next turn.")
        opponent.attack_power / 2 #This is wrong- need correct implementation here


# Mage class (inherits from Character)
class Mage(Character): #Good amount of health
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, heals_left=3, special1=self.cast_spell, special2=self.summon_minions) 

    def cast_spell(self, opponent):
        damage = 50
        opponent.health -= damage
        print(f'{self.name} casted a fireball! Deals {damage} damage.')
    
    def summon_minions(self, opponent):
        minion_damage = 10

        ##Generate random amount of minions and have them do damage
        random_min_list = [1,2,3,4,5,6,7,8,9,10]
        random.shuffle(random_min_list)
        first_value = random_min_list[0]

        opponent.health -= first_value * minion_damage
        
        print(f'\n{first_value} minions do 10 damage each! Dealing {first_value * 10} damage!')

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=55, heals_left=3)

    #Add a power archer shot here
    #One more special ability (Triple shot?)

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=75, attack_power=30, heals_left=3)

    #Special to stop Wizards attack for a turn (charm him with music)
    #Boost health/become invincible for several turns

'''
Possibly another Character class depending on time/functionality
'''

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=350, attack_power=15, heals_left=None, special1=None, special2=None)  
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        if self.health < self.max_health:
           self.health += 5
           if self.health > self.max_health:
              self.health = self.max_health ##Only Regen to max health
           print(f"{self.name} regenerates 5 health! Current health: {self.health}")
        else:
           print(f"{self.name} is at max health!")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Bard") 
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("\nEnter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)      
    elif class_choice == '4':
        return Bard(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_attack(wizard)
        elif choice == '3':
            player.heal()
            continue ##Allow another move after a heal.
        elif choice == '4':
            player.display_stats()
            continue ##Prevents Dark Wizard from regenerating when checking stats.
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()
    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")
    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()