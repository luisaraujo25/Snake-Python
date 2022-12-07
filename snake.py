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

def move_snake(direction, snakePosX, snakePosY, cellSize, snakeBody):

    auxX = snakePosX
    auxY = snakePosY

    moveX = 0
    moveY = 0

    if direction == "up":
        snakePosY -= cellSize
        moveY = -1
    elif direction == "down":
        snakePosY += cellSize
        moveY = 1
    elif direction == "left":
        snakePosX -= cellSize
        moveX = -1
    elif direction == "right":
        snakePosX += cellSize
        moveX = 1

    for index in range(len(snakeBody)):
        [nextX, nextY] = snakeBody[index]
        snakeBody[index] = [auxX, auxY]
        [auxX, auxY] = [nextX, nextY]

    return [(snakePosX, snakePosY), snakeBody]

def draw_body(colour, direction, radius, snakeBody, cellSize, window):
    
    for pos in snakeBody:  
        pg.draw.circle(window, colour, (pos[0] + radius, pos[1] + radius), radius)

def main():

    #width, height
    x = 500
    y = 500
    dimensions = (x, y)
    window = pg.display.set_mode(dimensions)
    backgroundColour = (255,255,255)
    clock = pg.time.Clock()


    white = (255,255,255)
    green = (0,200,0)

    cellSize = 25 
    noCells = dimensions[0] / cellSize
    #noCells = 20 rn
    radius = cellSize / 2
    snakePosX = 0
    snakePosY = 0
    cherryRadius = radius
    direction = "right"
    FPS = 8
    cherry = False
    snakeBody = []
    posX, posY = 0, 0

    random.seed()

    while(1):
        
        clock.tick(FPS)
        window.fill(backgroundColour)

        # See if there is the need to generate a new cherry
        if cherry == False:
            cherryPos = cherryGenerator(noCells, cellSize, cherryRadius)
            cherry = True

        # Check if any key was pressed and, if so, determine a new direction
        direction = check_key(direction)

        # Update snake position
        [(snakePosX, snakePosY), snakeBody] = move_snake(direction, snakePosX, snakePosY, cellSize, snakeBody)
        
        # Check if snake position needs to be changed
        (snakePosX, snakePosY) = check_boundaries(snakePosX, snakePosY, noCells, cellSize, direction)
        
        # Draw everything
        displayCherry(window, cherryPos, cherryRadius)
        pg.draw.circle(window, green, (snakePosX + radius, snakePosY + radius), radius)
        draw_body(green, direction, radius, snakeBody, cellSize, window)

        # Check if the snake eats the cherry
        if (snakePosX, snakePosY) == cherryPos:
            snakeBody.append([snakePosX, snakePosY])
            cherry = False
            
        pg.event.pump()
        pg.display.flip()

main()