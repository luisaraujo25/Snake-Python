import pygame as pg
import random

def cherryGenerator(noCells, cellSize, radius):

    posX = random.randint(0,noCells) * cellSize + radius
    posY = random.randint(0, noCells) * cellSize + radius

    return (posX,posY)

def displayCherry(window, pos, radius):

    red = (255,0,0)
    pg.draw.circle(window, red, pos, radius)

def check_boundaries(snakePosX, snakePosY, noCells, cellSize, direction):
    
    if snakePosX == 0 and direction == "left":
        snakePosX = noCells * cellSize
    elif snakePosX == noCells * cellSize and direction == "right":
        snakePosX = 0
    elif snakePosY == 0 and direction == "up":
        snakePosY = noCells * cellSize
    elif snakePosY == noCells * cellSize and direction == "down":
        snakePosY = 0

    return (snakePosX, snakePosY)

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

    cherryRadius = 10

    random.seed()
    white = (255,255,255)
    cherry = False

    while(1):
        
        clock.tick(FPS)

        (snakePosX, snakePosY) = check_boundaries(snakePosX, snakePosY, noCells, cellSize, direction)

        
        if cherry == False:
            cherryPos = cherryGenerator(noCells, cellSize, cherryRadius)
            displayCherry(window, cherryPos, cherryRadius)
            cherry = True

        if (snakePosX, snakePosY) == cherryPos:
            print("werdftgyhujioklpç")
            cherry = False

        key = pg.key.get_pressed()

        if key[pg.K_UP] and direction != "down":
            direction = "up"
        elif key[pg.K_DOWN] and direction != "up":
            direction = "down"
        elif key[pg.K_LEFT] and direction != "right": 
            direction = "left"
        elif key[pg.K_RIGHT] and direction != "left":
            direction = "right"

        if direction == "up":
            snakePosY -= cellSize 
        elif direction == "down":
            snakePosY += cellSize
        elif direction == "left":
            snakePosX -= cellSize
        elif direction == "right":
            snakePosX += cellSize

        pg.draw.circle(window, green, (snakePosX + radius, snakePosY + radius), radius)
        (auxX, auxY) = (snakePosX, snakePosY)

        pg.event.pump()
        pg.display.flip()
        pg.draw.circle(window, white, (auxX + radius, auxY + radius), radius)

main()