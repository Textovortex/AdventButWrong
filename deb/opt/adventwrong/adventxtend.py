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
try: from adventurelib import Item, say # importing dependencies
except: from adstrangerlib import Item, say
from random import choice


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

class Player(Character):
    '''
    The player class extends the character.
    '''
    def __init__(self, name, hp, dp, powers=None, exp=None, lvl=None):
        self.name = name
        self.hp = hp
        self.dp = dp
        self.powers = powers
        self.exp = exp
        self.lvl = lvl


class Battle():
    def __init__(self, lose_msg, win_msg, character_, player_, reset_func):
        '''
        lose_msg = messages when the player loses; is a list
        win_msg = when the player wins; is a list
        character_ = the character the player battles; is a Character object
        player_ = the player variable; is a Player object
        reset_func = function to reset your game if the player loses the battle.; is a function
        '''
        self.lose_msg = lose_msg
        self.win_msg = win_msg
        character = character_
        player = player_
        self.reset_func = reset_func

    def start(self):
        '''
        Starts the battle
        '''
        finished = False # the battle is not finished
        while not finished:
            if player.hp <= 0:
                say("You died.") # RIP you
                
                self.reset_func() # run the reset function, as it is going to 
                break
            elif character.hp <= 0: # Oh, yay, now do I have to beat that troll over there?
                say("You won!")
                break
            message = choice(choice([self.win_msg, self.lose_msg])) # generate a random message
            say(f'You are now fighting the {character}') # yes, I do need to know when I am fighting the 
            response = input(f"HP{player.hp}\nChoose a power")
            if response in player.powers:
                say(f'You {response} the {character.name}')
                character.hp -= player.dp
                say(f"The {character.name} has now {character.hp} health points")
                say(message)
                if message in self.win_msg:
                    player.hp += character.dp
                player.hp -= character.dp
                say(f"The {character.name} fights you back and you lose {character.dp} HP")
            else:
                say("Choose a valid power") # yeah, do you really expect me?
            
            
