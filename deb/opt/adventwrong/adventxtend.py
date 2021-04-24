'''
 ________  ________  ___      ___ _______   ________   _________   ___    ___ _________  _______   ________   ________     
|\   __  \|\   ___ \|\  \    /  /|\  ___ \ |\   ___  \|\___   ___\|\  \  /  /|\___   ___\\  ___ \ |\   ___  \|\   ___ \    
\ \  \|\  \ \  \_|\ \ \  \  /  / | \   __/|\ \  \\ \  \|___ \  \_|\ \  \/  / ||___ \  \_\ \   __/|\ \  \\ \  \ \  \_|\ \   
 \ \   __  \ \  \ \\ \ \  \/  / / \ \  \_|/_\ \  \\ \  \   \ \  \  \ \    / /     \ \  \ \ \  \_|/_\ \  \\ \  \ \  \ \\ \  
  \ \  \ \  \ \  \_\\ \ \    / /   \ \  \_|\ \ \  \\ \  \   \ \  \  /     \/       \ \  \ \ \  \_|\ \ \  \\ \  \ \  \_\\ \ 
   \ \__\ \__\ \_______\ \__/ /     \ \_______\ \__\\ \__\   \ \__\/  /\   \        \ \__\ \ \_______\ \__\\ \__\ \_______\
    \|__|\|__|\|_______|\|__|/       \|_______|\|__| \|__|    \|__/__/ /\ __\        \|__|  \|_______|\|__| \|__|\|_______|
                                                                  |__|/ \|__|  
                                                                  
                                                                               By | |_|_| /\_|_._  _ o.__|_ _    
                                                                                  |_|_| |/--\|_|_||_)(_)|| ||_(_)\/\/                                                                                                                        
                                                                                                                                                                   
    _/  _/                                                          _/                                _/                          _/      _/  _/_/_/  _/_/_/_/_/   
   _/        _/_/_/    _/_/    _/_/_/      _/_/_/    _/_/      _/_/_/      _/    _/  _/_/_/      _/_/_/    _/_/    _/  _/_/      _/_/  _/_/    _/        _/        
  _/  _/  _/        _/_/_/_/  _/    _/  _/_/      _/_/_/_/  _/    _/      _/    _/  _/    _/  _/    _/  _/_/_/_/  _/_/          _/  _/  _/    _/        _/         
 _/  _/  _/        _/        _/    _/      _/_/  _/        _/    _/      _/    _/  _/    _/  _/    _/  _/        _/            _/      _/    _/        _/          
_/  _/    _/_/_/    _/_/_/  _/    _/  _/_/_/      _/_/_/    _/_/_/        _/_/_/  _/    _/    _/_/_/    _/_/_/  _/            _/      _/  _/_/_/      _/           
                                                                                                                                                                   
                                                                                                                                                                   

'''
try: from adventurelib import Item, say, Bag # importing dependencies
except: from adstrangerlib import Item, say, Bag
from random import choice, randint
import time

__version__ = "0.0.3"

class Character(Item):
    '''
    The character.'''
    def __init__(self, name, desc, hp, dp, powers=None, exp=None):
        '''
        The character. Do NOT use the variable "character"'''
        self.name = name
        self.desc = desc
        self.hp = hp
        self.dp = dp
        self.powers = powers
        self.exp = exp
        self.list = Bag()

class Player(Character):
    '''
    The player class extends the character.
    '''
    def __init__(self, name, hp, dp_range, powers=None, exp=None, lvl=None):
        self.name = name
        self.hp = hp
        self.dp = dp_range
        self.powers = powers
        self.exp = exp
        self.lvl = lvl


class Battle():
    def __init__(self, lose_msg, win_msg, character_, player_, reset_func,
                 death_msg="You Died.",
                 vict_msg="You Won!",
                 prompt ="Enter a power >",
                 unknown_power="Choose a valid power"):
        '''
        lose_msg = messages when the player loses; is a list
        win_msg = when the player wins; is a list
        character_ = the character the player battles; is a Character object
        player_ = the player variable; is a Player object
        reset_func = function to reset your game if the player loses the battle.; is a function
        '''
        self.lose_msg = lose_msg
        self.win_msg = win_msg
        self.character = character_
        self.character_save = character_
        self.player = player_
        self.reset_func = reset_func
        self.death_msg = death_msg
        self.vict_msg = vict_msg
        self.prompt = prompt
        self.unk_power = unknown_power

    def start(self):
        global player
        '''
        Starts the battle
        '''
        self.finished = False # the battle is not finished
        while not self.finished:
            if self.player.hp <= 0:
                say(self.death_msg) # RIP you
                
                self.reset_func() # run the reset function, as it is going to
                self.finished = True
                self.character.hp = self.character_save.hp
                break
            elif self.character.hp <= 0: # Oh, yay, now do I have to beat that troll over there?
                say(self.vict_msg)
                self.finished = True
                self.character.hp = self.character_save.hp
                break

            say(f"You have {self.player.hp} \u2665")
            time.sleep(0.5)
            
            #message = choice(choice([self.win_msg, self.lose_msg])) # generate a random message
            say(f"You are fighting the {self.character.name}") # yes, I do need to know when I am fighting the 
            #response = input(f"\u2665 {self.player.hp}\nChoose a power > ")
            #if response in self.player.powers:
            #    say(f'You {response} the {self.character.name}')
            #    self.character.hp -= self.player.dp
            #    say(f"The {self.character.name} has now {self.character.hp} health points")
            #    say(message)
            #    if message in self.win_msg:
            #        self.player.hp += self.character.dp
            #    self.player.hp -= self.character.dp
            #    say(f"The {self.character.name} fights you back and you lose {self.character.dp} HP")
            #else:
            #    say("Choose a valid power") # yeah, do you really expect me?

            self.fighter = choice([self.player, self.character])
            time.sleep(0.5)

            if self.fighter is self.player:
                for power in self.player.powers:
                    say(f"You have the power to {power}")
                    time.sleep(0.3)
                power = input(self.prompt)
                if power in self.player.powers:
                    self.character.hp -= randint(self.player.dp[0],self.player.dp[1])
                    say(choice(self.win_msg))
                else:
                    say(self.unk_power)

            else:
                self.player.hp -= self.character.dp
                time.sleep(1)
                say(choice(self.lose_msg))
            
            time.sleep(1)    
            say(f"The {self.character.name} has {self.character.hp} \u2665")    
                
            
