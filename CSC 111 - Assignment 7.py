# ----------------------------------------------------------------------------------
#        Name: Nukhbah Majid (I did not collaborate with anybody on this assignment)
#    Filename: CSC 111 - Assignment 7: Slow Pokemon
#        Date: 11/06/18
# Description: Constructing a Pokemon arcade simulation, that allows combat between 
#              Pokemon's of the two rivals and displays the stats accordingly as the
#              game progresses. Main elements: selecting Pokemon, attacking and
#              defending, stats display. 
# ----------------------------------------------------------------------------------

from random import randint


class Pokemon:

    def __init__(self, name):
        self.name = name
        self.pokemon_type = "NORMAL"
        self.max_hp = randint(99,500)
        self.current_hp = self.max_hp
        self.attack_power = randint(10,self.max_hp - 1)
        self.defend_power = randint(10,self.max_hp - 1)
        self.revives = 0
        self.fainted = False

    def printStats(self):
        print("Name:", self.name)
        print("Type:", self.pokemon_type)
        print("Max HP:", self.max_hp)
        print("Current HP:", self.current_hp)

    def defend(self):
        self.current_hp = self.current_hp - self.defend_power
        if (self.current_hp <= 0): 
            self.current_hp = 0
            print("Whoops.. \nYour Pokemon,",self.name + ", just fainted.")
            self.fainted = True
        

    def attack(self, opponent):
        opponent.defend()
        

    def revive(self):
        if self.fainted == True:
            self.current_hp = int(self.max_hp/2)
            self.fainted = False
            return True
        else:
            return False

class Grass(Pokemon):

    def __init__(self, name):
        Pokemon.__init__(self,name)
        #super(Grass, self).__init__(name)
        self.pokemon_type = "GRASS"

    def attack(self, opponent):
        if (opponent.pokemon_type == "FIRE"):
            opponent.current_hp += randint(10,100)   #does less damage to a fire type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "WATER"):
            opponent.current_hp -= randint(10,100)   #does more damage to a water type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "GROUND"):
            opponent.current_hp -= randint(10,100)   #does more damage to a ground type pokemon
            opponent.defend()

        else:
            opponent.defend()


class Fire(Pokemon):

    def __init__(self, name):
        Pokemon.__init__(self,name)
        #super(Fire, self).__init__(name)
        self.pokemon_type = "FIRE"
        
    def attack(self, opponent):
        if (opponent.pokemon_type == "WATER"):
            opponent.current_hp += randint(10,100)   #does less damage to a water type pokemon
            opponent.defend()
            
        elif (opponent.pokemon_type == "WATER"):
            opponent.current_hp += randint(10,100)   #does less damage to a water type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "GRASS"):
            opponent.current_hp -= randint(10,100)   #does more damage to a grass type pokemon
            opponent.defend()

        else:
            opponent.defend()


class Water(Pokemon):

    def __init__(self, name):
        Pokemon.__init__(self,name)
        #super(Water, self).__init__(name)
        self.pokemon_type = "WATER" 

    def attack(self, opponent):
        if (opponent.pokemon_type == "GRASS"):
            opponent.current_hp += randint(10,100)   #does less damage to a grass type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "ELECTRIC"):
            opponent.current_hp += randint(10,100)   #does less damage to a electric type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "FIRE"):
            opponent.current_hp -= randint(10,100)   #does more damage to a fire type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "GROUND"):
            opponent.current_hp -= randint(10,100)   #does more damage to a ground type pokemon
            opponent.defend()

        else:
            opponent.defend()


class Electric(Pokemon):

    def __init__(self, name):
        Pokemon.__init__(self, name)
        #super(Water, self).__init__(name)
        self.pokemon_type = "ELECTRIC"

    def attack(self, opponent):
        if (opponent.pokemon_type == "GROUND"):
            opponent.current_hp += randint(10,100)   #does less damage to ground type pokemon
            opponent.defend()
        
        elif (opponent.pokemon_type == "WATER"):
            opponent.current_hp -= randint(10,100)   #does more damage to water type pokemon
            opponent.defend()
            
        else:
            opponent.defend()



class Ground(Pokemon):

    def __init__(self, name):
        Pokemon.__init__(self, name)
        #super(Ground, self).__init__(name)
        self.pokemon_type = "GROUND"

    def attack(self, opponent):
        if (opponent.pokemon_type == "GRASS"):
            opponent.current_hp += randint(10,100)   #does less damage to grass type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "WATER"):
            opponent.current_hp += randint(10,100)   #does less damage to water type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "ELECTRIC"):
            opponent.current_hp -= randint(10,100)   #does more damage to electric type pokemon
            opponent.defend()

        elif (opponent.pokemon_type == "FIRE"):
            opponent.current_hp -= randint(10,100)   #does more damage to electric type pokemon
            opponent.defend()

        else:
            opponent.defend()

    
            
            
def battle(player1, player2):
    while player1.fainted or player2.fainted != True:
        if player1.fainted != True:
            player1.attack(player2)
            player2.printStats()
            print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
            if player2.fainted == True:
                player2_input = input("Revive your Pokemon, " + player2.name + "? (Y/N): ")
                print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                player2_input = player2_input.upper()
                if player2_input == "Y" and player2.revives < 2:
                    player2.revive()
                    player2.revives += 1
                elif player2_input == "Y" and player2.revives >= 2:
                    print(player2.name, """has availed all the revives. :(( \nThe duel is now over.""")
                    print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                    print(player1.name, "is the WINNER!!!")
                    print("""
                        ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗         ██╗
                        ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗    ██╗██╔╝
                           ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║    ╚═╝██║ 
                           ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║    ██╗██║ 
                           ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝    ╚═╝╚██╗
                           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝         ╚═╝ """)
                    
                    break
                else:
                    print("Rest in Peace. You just got rekt. The duel is over.")
                    print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                    print(player1.name, "is the WINNER!!!")
                    print("""
                        ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗         ██╗
                        ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗    ██╗██╔╝
                           ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║    ╚═╝██║ 
                           ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║    ██╗██║ 
                           ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝    ╚═╝╚██╗
                           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝         ╚═╝ """)
                    
                    break
            ##**interesting additional information**##
            if player2.fainted != True:
                player2.attack(player1)
                player1.printStats()
                print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                ##**interesting additional information**##
                if player1.fainted == True:
                    player1_input = input("Revive your Pokemon, " + player1.name + "? (Y/N): ")
                    print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                    player1_input = player1_input.upper()
                    if player1_input == "Y" and player1.revives < 2:
                        player1.revive()
                        player1.revives += 1
                    elif player1_input == "Y" and player1.revives >= 2:
                        print(player1.name, """has availed all the revives. :(( \nThe duel is now over.""")
                        print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                        print(player2.name, "is the WINNER!!!")
                        print("""
                        ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗         ██╗
                        ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗    ██╗██╔╝
                           ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║    ╚═╝██║ 
                           ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║    ██╗██║ 
                           ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝    ╚═╝╚██╗
                           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝         ╚═╝ """)
                        
                                                                  
                        break
                    else:
                        print("Rest in Peace. You just got rekt. The duel is over.")
                        print("\n=^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=    =^..^=   =^..^=   =^..^=    =^..^=    =^..^=    =^..^=    =^..^=\n")
                        print(player2.name, "is the WINNER!!!")
                        print("""
                        ████████╗██╗  ██╗███████╗    ███████╗███╗   ██╗██████╗         ██╗
                        ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝████╗  ██║██╔══██╗    ██╗██╔╝
                           ██║   ███████║█████╗      █████╗  ██╔██╗ ██║██║  ██║    ╚═╝██║ 
                           ██║   ██╔══██║██╔══╝      ██╔══╝  ██║╚██╗██║██║  ██║    ██╗██║ 
                           ██║   ██║  ██║███████╗    ███████╗██║ ╚████║██████╔╝    ╚═╝╚██╗
                           ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝╚═════╝         ╚═╝ """)
                        
                        break
        
    

        

                   
def main():
    print("")
    print("""

████████╗██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗    ██████╗ ███████╗ ██████╗ ██╗███╗   ██╗███████╗██╗██╗
╚══██╔══╝██║  ██║██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔══██╗██╔════╝██╔════╝ ██║████╗  ██║██╔════╝██║██║
   ██║   ███████║█████╗      ██║  ███╗███████║██╔████╔██║█████╗      ██████╔╝█████╗  ██║  ███╗██║██╔██╗ ██║███████╗██║██║
   ██║   ██╔══██║██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██╔══██╗██╔══╝  ██║   ██║██║██║╚██╗██║╚════██║╚═╝╚═╝
   ██║   ██║  ██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ██████╔╝███████╗╚██████╔╝██║██║ ╚████║███████║██╗██╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝╚═╝ """)
    
    print("")                                                                                                                     
    print("""
 
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|""")


    print("")
    print("""YOU CAN CHOOSE THE FOLLOWING POKEMON:
                SQUIRTLE (TYPE: WATER)
                BULBASAUR (TYPE: GRASS)
                CHARMANDER (TYPE: FIRE)
                PIKACHU (TYPE: ELECTRIC)
                ONIX (TYPE: GROUND)
                        OR
                A NORMAL POKEMON WITH A NAME OF YOUR OWN CHOICE\n""")
    player1_input = input("Player 1, select a Pokemon: ")
    player2_input  = input("Player 2, select a Pokemon: ")
    player1_input = player1_input.upper()
    player2_input = player2_input.upper()

    if player1_input == "SQUIRTLE":
        player1 = Water(player1_input)
    elif player1_input == "BULBASAUR":
        player1 = Grass(player1_input)
    elif player1_input == "CHARMANDER":
        player1 = Fire(player1_input)
    elif player1_input == "PIKACHU":
        player1 = Electric(player1_input)
    elif player1_input == "ONIX":
        player1 = Ground(player1_input) 
    else:
        player1 = Pokemon(player1_input)


    if player2_input == "SQUIRTLE":
        player2 = Water(player2_input)
    elif player2_input == "BULBASAUR":
        player2 = Grass(player2_input)
    elif player2_input == "CHARMANDER":
        player2 = Fire(player2_input)
    elif player2_input == "PIKACHU":
        player2 = Electric(player2_input)
    elif player2_input == "ONIX":
        player2 = Ground(player2_input)
    else:
        player2 = Pokemon(player2_input)

    print("")
    battle(player1, player2)
        


if __name__ == "__main__":
    main()


#--------------------------------------------------------------------------------------------------------------------------
# References : I was having trouble figuring out why my subclasses were not inheriting the attributes from the parent class
#              and found this really helpful documentation on how to use an built-in function called "super()", found here:
#              https://docs.python.org/3/library/functions.html#super
#              Although I managed to resolve the inheriting of parent class' attributes problem in a different
#              way, I still left the code that I wrote using super() as a comment as a trace of my thought process. I was
#              able to resolve why I couldn't inherit the parent class' attributes by the help of the question asked by
#              U9-Forward here:
#              https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
#
#              In order to better understand what type of pokemon was strong/weak against other types I referred to
#              the following pages:
#              1. https://www.primagames.com/games/pokemon-go/tips/best-pokemon-pokemon-go-strategies-and-battle-type-chart
#              2. http://pokemon.wikia.com/wiki/Types
#
#              I used the ASCII text generator for the UI: http://patorjk.com/software/taag/
#--------------------------------------------------------------------------------------------------------------------------

