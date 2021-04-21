from adstrangerlib import *
from adventxtend import *
import time


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

player_name = "Player" # yeah, thats a thing...

player = Player(player_name, 20, 5, ("hit", "punch"), 100, 1)

Battle.playet = player


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#R
#O
#O
#M
#S (I had no time for ascii)

'''
VOID
ROOMS
'''
white_void = Room('You are in some kind of white void. You don\'t feel great. The void feels cold and uncomfortable') #the totally real start of the game

white_void_alt = Room("This is something lke the white void you were in before. There's no way to escape. In the air there lies a pair of shoes with heels") #huh, looks like there is an alt to the white original...

'''
STARTER ROOMS
'''

forest = Room("You are now lost in a forest")

magic_forest = Room("You are now lost in a forest") # you are now lost in a magic forest
magic_clearing = Room("You are in a clearing. You see a chest.")

road_start = Room("This is a road going down northeast. To the southwest there is a road too but you are too tired to go there. To the all other directions there is a forest.")
road_segment1 = Room("This is a road going northeast and southwest. You see an old traveler here")
road_segment2 = Room("This is a road going northeast and southwest. You see a pile of rocks here")
road_segment3 = Room("This is a road going northeast and southwest. You step in the cool shade.")
road_segment4 = Room("This is a road going northeast and southwest. You are in a dark shade")
road_segment5 = Room("This is a road going northeast and southwest. To the southwest you see a big city surrounded by a wall. There is a river going around the city and a bridge to cross it")

bridge = Room("You are on a bridge that goes across the river. To the south there is a road that goes further southwest. To the north there is a gate that leads into the city.")
gate = Room("This is the gate. Two guards are here")


'''
ANAMOKLEA
ROOMS
'''

south_anamoklea = Room("You are in the south Anamoklea. You see passages in all directions, except south.")
east_anamoklea = Room("You are in the east Anamoklea. To the north there is an entrance to a palace, with a guard here.")
north_anamoklea = Room("You are in the north Anamoklea. There is a shop to the east.")
west_anamoklea = Room("You are in the west Anamoklea. To the north there is an old house with a slightly ajar door")

broken_house = Room("You are in the broken house. There is a eyepop spawner here.")



'''
MISCELLANNOUS
ROOMS
'''
forest = Room("You are now lost in a forest")
magic_forest = Room("You are now lost in a forest") # you are now lost in a magic forest
magic_elf_forest = Room("You are now lost in a magically amazing forest")

magic_clearing = Room("You are in a clearing. You see a chest.")

magic_cave_start = Room("You are in a cave that most likely you entered through a chest. Any light source that is here fades.")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ITEMS
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

heels = Item("A pair of shoes with heels", "heels")

ax = Item("An axe with acient gravings on it", "Axe")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Room.can_scream = True

white_void.can_scream = False # You cannot scream in any kind of void, it fades
white_void_alt.can_scream = False

magic_clearing.add_direction('down', 'up')



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Characters
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

eyepop = Character("Eyepop", "An ordinary Eyepop", 10, 5)

palace_guard = Character("A palace guard", "An ordinary human guard", 10, 5)

king = Character("King", "A fat king. Husband of queen Tess", 50, 10)
bess = Character("Queen Bess", "Queen Bess, sister of the dead Queen Tess", 100, 15)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#setting up the directions in the void. Also, you cannot escape the alt.... unless you take the heels.
white_void.north = white_void
white_void.east = white_void
white_void.south = white_void
white_void.west = white_void_alt

road_start.north = magic_forest
road_start.south = forest
road_start.east = road_segment1


magic_forest.south = road_start
magic_forest.north = magic_clearing
magic_forest.east = forest
magic_forest.west = forest

magic_clearing.south = magic_forest
magic_clearing.north = forest
magic_clearing.east = forest
magic_clearing.west = forest
magic_clearing.down = magic_cave_start


road_segment1.west = road_start
road_segment1.east = road_segment2

road_segment2.west = road_segment1
road_segment2.east = road_segment3

road_segment3.west = road_segment2
road_segment3.east = road_segment4

road_segment4.west = road_segment3
road_segment4.east = road_segment5

road_segment5.west = road_segment4
road_segment5.east = bridge
road_segment5.north = bridge

bridge.south = road_segment5
bridge.north = gate

forest.south = forest #so sad, no escape you are lost...
forest.north = forest
forest.east = forest
forest.west = forest

gate.south = bridge

south_anamoklea.east = east_anamoklea
south_anamoklea.west = west_anamoklea
south_anamoklea.north = north_anamoklea

north_anamoklea.south = south_anamoklea

east_anamoklea.west = west_anamoklea

west_anamoklea.east = east_anamoklea
west_anamoklea.north = broken_house





#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


current_room = west_anamoklea # bruh, why would i start a game in a place like zork, full of clues.


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTIONS
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
SYSTEM FUNCTIONS
'''

def exec_process():
    global current_room, player_name
    if current_room == gate:
        say("Guard 1: Hello, stranger, we need a few checks before you can pass.")
        time.sleep(3)
        say("You look supspicious.")
        time.sleep(1)
        say("What is your name?")
        player_name = player.name = input("Enter your name: ")
        time.sleep(2)
        say(f"Oh, I see, {player.name}, you can enter. You do not look supspicious now.")
        time.sleep(4)
        current_room = south_anamoklea
        say("You enter the gate as it shuts behind you.")
        time.sleep(2)
        look()
    if current_room == broken_house:
        eyepop_battle.start()
        player = eyepop_battle.player

def reset():
    current_room = white_void
    player.inventory = Bag()
    print("------------------YOU DIED------------------")

'''
@WHEN Functions
'''

@when('go DIRECTION') # how did you expect me to make the guy move? Probably not using the queen's carriage...
def go(direction):
    global current_room
    if current_room.north and direction in ['n','nor','nort','forward','north']:
        current_room = current_room.north
    elif current_room.west and direction in ['w','wes','west','right']:
        current_room = current_room.west
    elif current_room.east and direction in ['e','eas','east','left']:
        current_room = current_room.east
    elif current_room.south and direction in ['s','sou','south','back']:
        current_room = current_room.south
    else:
        say("You can't go that way") # really? go poop?
    look() #and another time we look around

@when('look') # you look everywhere until you type this code: 
def look():
    global current_room
    say(current_room)
    exec_process()

@when('scream')
@when('cry')
def scream():
    try:
        if current_room.can_scream:
            say('You scream as the around shivers')
        else:
            say('You try to scream but it fades as you try')
    except:
        say("You don't want to scream here...")
@when("click ITEM")
def click(item):
    global current_room
    if item == "heels" and current_room == white_void_alt:
        current_room = road_start
        look()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Battles
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

eyepop_battle = Battle(("Oops, the eyepop tried to take out your eye.",
                        "It looks like you slipped on a wooden plank and fell.",
                        "The eyepop jumped on you, and paralized you for a second.",
                        "You tried to kiss the eyepop."),
                       ("You jumped on the eyepop, trying to squash him.",
                        "You farted on the eyepop.",
                        "You punched the eyepop hard.",
                        "The eyepop tried to smell a mouse that didn't exist."),
                       eyepop, player, reset)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


look() # look around to tell the player where is he
start(help=False) # start the game
