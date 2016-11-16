from hlt import *
from networking import *

myID, gameMap = getInit()
sendInit("MyBotSubmit")

#lastDied = Location(0, 0)

##def directionTo(toward):
##    x = location.x
##    y = location.y
##    oX = lastDied.x
##    oY = lastDied.y


# Moving shit
# implement some chess shit
def move(location):
    site = gameMap.getSite(location)

    empty = []

    # Get strength of frienlys

    #adjust weights accordingly

    # Attack any neighbor weaker than you
    for direct in CARDINALS:
        neighbor = gameMap.getSite(location, direct)
        if neighbor.owner != myID and neighbor.strength+1 < site.strength:
            empty.append(neighbor)
            return Move(location, direct)

    #Never combine with other biguns
    # If your Big
    if site.strength > 225:
        return Move(location, WEST if random.random() > 0.2 else NORTH)

    # Check Neighbors, think, choose best move
    for direct in CARDINALS:
        neighbor = gameMap.getSite(location, direct)


        if neighbor.owner == myID:
            if neighbor.strength + site.strength > 224:
                continue
            
            elif site.strength > (site.production-1)*6:
                # direction to edge
                if gameMap.getSite(location, (direct+2)%5).strength - (site.production)^2 < site.strength:
                    #lastDied = gameMap.getLocation(location, (direct+2)%5)
                    return Move(location, (direct+2)%5 if random.random() > 0.4 else STILL)
                else:
                    return Move(location, (direct+3)%5 if random.random() > 0.6 else STILL)
                
            elif site.strength < site.production * 5:
                return Move(location, STILL)
        else:
            if site.strength > neighbor.strength + 1:
                #lastDied = gameMap.getLocation(location, direct)
                return Move(location, direct)
    # If your Big
    if site.strength > 127:
        return Move(location, NORTH if random.random() > 0.5 else WEST)
    else:
        return Move(location, SOUTH if random.random() > 0.6 else EAST)


# Game loop
while True:
    moves = []
    gameMap = getFrame()
    for y in range(gameMap.height):
        for x in range(gameMap.width):
            location = Location(x, y)
            if gameMap.getSite(location).owner == myID:
                moves.append(move(location))
    sendFrame(moves)
