from adventurelib import *

white_void = Room('You are in some kind of void. You don\'t feel great. The void feels cold and uncomfortable') #the totally real start of the game

white_void_alt = Room("This is something lke the void you were in before. There's no way to escape. In the air there lies a pair of shoes with heels") #huh, looks like there is an alt to the white original...

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
END STARTER ROOMS
'''

forest = Room("You are now lost in a forest")
magic_forest = Room("You are now lost in a forest") # you are now lost in a magic forest
magic_elf_forest = Room("You are now lost in a magically amazing forest")

magic_clearing = Room("You are in a clearing. You see a chest.")

magic_cave_start = Room("You are in a cave that most likely you entered through a chest. Any light source that is here fades.")

Room.can_scream = True

white_void.can_scream = False # You cannot scream in any kind of void, it fades
white_void_alt.can_scream = False

magic_clearing.add_direction('down', 'up')

#setting up the directions in the void. Also, you cannot escape the alt.... unless you take the heels.
white_void.north = white_void
white_void.east = white_void
white_void.south = white_void
white_void.west = white_void_alt

road_start.north = magic_forest
road_start.south = forest
road_start.east = road_segment1

forest.south = forest #so sad, no escape you are lost...
forest.north = road_start #or maybe not
forest.east = forest
forest.west = forest

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

gate.south = bridge




current_room = white_void # bruh, why would i start a game in a place like zork, full of clues.


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



look() # look around to tell the player where is he
start(help=False) # start the game
