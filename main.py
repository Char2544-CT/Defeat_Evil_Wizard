# Base Character class
class Character:
    def __init__(self, name, health, attack_power, heals_left):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health # Store the original health for maximum limit
        self.heals_left = heals_left  # Store Heals left for each character

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):

        if self.heals_left > 0:
            self.health += 20
            self.heals_left -= 1
            if self.health > self.max_health:
               self.health = self.max_health ##Only Regen to max health
            print(f"{self.name} \nregenerates 20 health! Current health: {self.health} \nHeals left: {self.heals_left}")
        else:
            print(f"{self.name} \nhas no heals left!")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=45, heals_left=3)  # Boost health and attack power

    # Add your power attack method here
    #Two Unqiue Abilities for each Character


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, heals_left=3)  # Boost attack power

    # Add your cast spell method here
    # Summon Minions?

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
        super().__init__(name, health=350, attack_power=15, heals_left=None)  # Lower attack power
    
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
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("\nEnter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        # Add Archer class here        
        pass
    elif class_choice == '4':
        # Add Paladin class here
        pass
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
            # Call the special ability here
            pass  # Implement this
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