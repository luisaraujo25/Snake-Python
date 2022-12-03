import pygame as pg
import random

def cherryGenerator(noCells, cellSize, radius):

    posX = random.randint(0,noCells - 1) * cellSize
    posY = random.randint(0, noCells - 1) * cellSize

    return (posX,posY)

def displayCherry(window, pos, radius):

    red = (255,0,0)
    pg.draw.circle(window, red, (pos[0] + radius, pos[1] + radius), radius)

def check_boundaries(snakePosX, snakePosY, noCells, cellSize, direction):
    
    if snakePosX <= 0 and direction == "left":
        snakePosX = noCells * cellSize
    elif snakePosX >= noCells * cellSize and direction == "right":
        snakePosX = 0
    elif snakePosY <= 0 and direction == "up":
        snakePosY = noCells * cellSize
    elif snakePosY >= noCells * cellSize and direction == "down":
        snakePosY = 0

    return (snakePosX, snakePosY)

def check_key(direction):

    key = pg.key.get_pressed()

    if key[pg.K_UP] and direction != "down":
        direction = "up"
    elif key[pg.K_DOWN] and direction != "up":
        direction = "down"
    elif key[pg.K_LEFT] and direction != "right": 
        direction = "left"
    elif key[pg.K_RIGHT] and direction != "left":
        direction = "right"

    return direction

def move_snake(direction, snakePosX, snakePosY, cellSize):

    if direction == "up":
        snakePosY -= cellSize 
    elif direction == "down":
        snakePosY += cellSize
    elif direction == "left":
        snakePosX -= cellSize
    elif direction == "right":
        snakePosX += cellSize

    return (snakePosX, snakePosY)

def draw_snake(window, colour, snakePosX, snakePosY, direction, radius, snakeBody, cellSize):

    pg.draw.circle(window, colour, (snakePosX + radius, snakePosY + radius), radius)

    posX, posY = snakePosX, snakePosY
    
    for i in range(snakeBody):        

        if direction == "up":
            posY += cellSize
        elif direction == "down":
            posY -= cellSize
        elif direction == "left":
            posX += cellSize 
        elif direction == "right":
            posX -= cellSize
        
        pg.draw.circle(window, colour, (posX + radius, posY + radius), radius)


    return (posX, posY)

def main():

    #width, height
    x = 500
    y = 500
    dimensions = (x, y)
    window = pg.display.set_mode(dimensions)
    backgroundColour = (255,255,255)
    window.fill(backgroundColour)

    cellSize = 25 
    noCells = dimensions[0] / cellSize
    #noCells = 20 rn

    green = (0,200,0)
    radius = cellSize / 2
    snakePosX = 0
    snakePosY = 0
    direction = "right"

    FPS = 8
    clock = pg.time.Clock()

    cherryRadius = radius

    random.seed()
    white = (255,255,255)
    cherry = False

    snakeBody = 0

    posX, posY = 0, 0

    while(1):
        
        clock.tick(FPS)
        pg.draw.circle(window, white, (posX + radius, posY + radius), radius)

        # See if there is the need to generate a new cherry
        if cherry == False:
            cherryPos = cherryGenerator(noCells, cellSize, cherryRadius)
            displayCherry(window, cherryPos, cherryRadius)
            cherry = True

        # Check if any key was pressed and, if so, determine a new direction
        direction = check_key(direction)

        # Update snake position
        (snakePosX, snakePosY) = move_snake(direction, snakePosX, snakePosY, cellSize)
        
        # Check if snake position needs to be changed
        (snakePosX, snakePosY) = check_boundaries(snakePosX, snakePosY, noCells, cellSize, direction)
        
        # Draw snake in the new position
        (posX, posY) = draw_snake(window, green, snakePosX, snakePosY, direction, radius, snakeBody, cellSize)

        # Check if the snake eats the cherry
        if (snakePosX, snakePosY) == cherryPos:
            snakeBody += 1
            cherry = False
            
        pg.event.pump()
        pg.display.flip()

main()