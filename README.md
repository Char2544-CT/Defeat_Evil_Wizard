# Defeat The Evil Wizard

## Methods for combat

### Base character class is created with added attributes of heals_left, special1, special2, and specials_left- meaning all characters will have these attributes.

-special_attack function:
A while loop runs, ensuring if there is an invalid choice, the loop runs again. We are looking for an input of either '1' or '2' considering each character has 2 special abilities. Since the character and functions are not known we use a format print statement to get the title of the function, replacing the pythonic underscore with a space and capitalizing the function.

-heal function:
Each character (besides the Evil Wizard) is grated 3 heals total. So when the heal method is called, the player heals for 20 and heals left decrements by 1. If health is at max, health will default to max health, ensuring the player doesn't go beyond their max. If a player heals, they are allowed to make another move without the wizard attacking or regenerating.

-limit_specials function:
In order for players to not spam their specials, a limit specials function is needed, and set to 5 for all players. Each time a special is used, specials_left decrements, shows the total left, and calls the character name by their class as a warning of sorts. Sort of like a narrator. Boolen values are returned.

## Character Classes

##### Warrior Class

-self.defending_rounds is added as a flag and set to 0 for later use.

-power_ax function:
a Simple function amplifying damage and subtracting it from the opponents health. Then printing a statement.

-defensive_stance function:
self.defending_rounds is set to 2 as a flag and runs functionality later, essentially floor dividing the wizards attack by 6, taking it to (2) total, for 2 rounds.

##### Mage Class

-cast_spell function:
another simple enchanced damage function.

-summon_minions function:
declares the amount of damage a minion does (10) then shuffles an array using random, ranging 1-10, takes the first number, stores it in a variable, and subtracts the random number times the minion damage from the wizards health.

##### Archer Class

-rain_of_arrows function:
Same idea with summon minions function except stores a random int in a variable from 1-10. Damage times 10 of that number and subtracts it from the opponents health.

-double_shot function:
Doubles attack power

##### Bard Class

-music_charm function:
The purpose of this function is to ultimately stop the wizard from attacking for a set number of turns. to do this, we store the wizards original_attack_power in a temporary variable and set his attack_power to 0. after 3 turns in the battle loop, the wizards attack_power is restored and original_attack_power variable is deleted but will be created again, if the function is called again. Each battle phase checks if the wizard has the attribute of 'charmed_turns' and functions accordingly.

-shield function:
Acts like a shield and essentially allows the Bard to go beyond their max HP.

##### Evil Wizard

-Has no heals_left, specials, or specials_left attributes. He always regenerates and starts with a lot of health.

-regenerate function:
Also inherits from the base class but has limited function. He cannot go over his allotted max health, and a message displays if he is already at max health.

## Battle functions and notes

-If a player uses specials, as long as the function returns True, the special_attack function is run on the Wizard. Else a message is displayed that the user is out of specials.

-'continue' allows a player to heal and check stats without the wizard taking action.

-besides checking if the wizard is 'charmed' on each battle phase, it also checks if the player is 'defending' i.e. only the Warrior. Having a total of 2 defensive rounds if the Warrior calls that special. He takes 2 total damage per round for 2 rounds. If neither of the charmed of defensive flags exist, the wizard attacks like normal.
