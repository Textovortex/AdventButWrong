from adventurelib import *

white_void = Room('You are in some kind of void. You don\'t feel great. The void feels cold and uncomfortable') #the totally real start of the game

white_void_alt = Room("This is something lke the void you were in before. There's no way to escape. In the air there lies a pair of shoes with heels") #huh, looks like there is an alt to the white original...

white_void.can_scream = False # You cannot scream in any kind of void, it fades
white_void_alt.can_scream = False

#setting up the directions in the void. Also, you cannot escape the alt.... unless you take the heels.
white_void.north = white_void
white_void.east = white_void
white_void.south = white_void
white_void.west = white_void_alt

current_room = white_void # bruh, why would i start a game in a place like zork, full of clues.


@when('go DIRECTION') # how did you expect me to make the guy move? Probably not using the queen's carriage...
def go(direction):
    global current_room
    if current_room.north and direction in ['n','nor','nort','forward','north']:
        current_room = current_room.north
    elif current_room.west and direction in ['w','wes','west','right']:
        current_room = current_room.west
    elif current_room.west and direction in ['e','eas','east','left']:
        current_room = current_room.east
    elif current_room.south and direction in ['s','sou','south','back']:
        current_room = current_room.south
    else:
        say("You can't go that way") # really? go poop?
    look() #and another time we look around

@when('look')
def look():
    global current_room
    print(current_room)

@when('scream')
@when('cry')
def scream():
    if current_room.can_scream:
        print('You scream as the around shivers')
    else:
        say('You try to scream but it fades as you try')
        
look() # look around to tell the player where is he
start() # start the game
