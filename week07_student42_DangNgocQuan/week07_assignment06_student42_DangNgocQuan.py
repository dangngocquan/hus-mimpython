import sys
import pygame
import numpy as np

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 4
CELL_SIZE = 15
NUMBER_ROW = SCREEN_HEIGHT // CELL_SIZE
NUMBER_COLUMN = SCREEN_WIDTH // CELL_SIZE
ANT0 = pygame.image.load("./additionalFolder/assignment06/source/ant/ant0.png")
ANT0 = pygame.transform.scale(ANT0, (CELL_SIZE, CELL_SIZE))
ANT1 = pygame.image.load("./additionalFolder/assignment06/source/ant/ant1.png")
ANT1 = pygame.transform.scale(ANT1, (CELL_SIZE, CELL_SIZE))
ANT2 = pygame.image.load("./additionalFolder/assignment06/source/ant/ant2.png")
ANT2 = pygame.transform.scale(ANT2, (CELL_SIZE, CELL_SIZE))
ANT3 = pygame.image.load("./additionalFolder/assignment06/source/ant/ant3.png")
ANT3 = pygame.transform.scale(ANT3, (CELL_SIZE, CELL_SIZE))
ANT = [ANT0, ANT1, ANT2, ANT3]

statusMatrix = np.zeros((NUMBER_ROW, NUMBER_COLUMN))  
antCoordinate = [NUMBER_COLUMN//2 * CELL_SIZE, NUMBER_ROW//2 * CELL_SIZE]
antDirection = 3
# 0 - UP
# 1 - RIGHT
# 2 - DOWN
# 3 - LEFT

def drawGrid(screen):
    for i in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, pygame.Color("gray"), (i, 0), (i, SCREEN_HEIGHT))
    for i in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, pygame.Color("gray"), (0, i), (SCREEN_WIDTH, i))

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

def update():
    global antDirection
    row = antCoordinate[1] // CELL_SIZE
    column = antCoordinate[0] // CELL_SIZE
    if statusMatrix[row, column] == 0:
        antDirection = (antDirection + 1) % 4
    else:
        antDirection = (antDirection - 1) % 4
    statusMatrix[row, column] = 1 - statusMatrix[row, column]
    
    if antDirection == 0:
        antCoordinate[1] = (antCoordinate[1] - CELL_SIZE) % SCREEN_HEIGHT
    elif antDirection == 1:
        antCoordinate[0] = (antCoordinate[0] + CELL_SIZE) % SCREEN_WIDTH
    elif antDirection == 2:
        antCoordinate[1] = (antCoordinate[1] + CELL_SIZE) % SCREEN_HEIGHT
    else:
        antCoordinate[0] = (antCoordinate[0] - CELL_SIZE) % SCREEN_WIDTH

def displayScreen(screen):
    screen.fill(pygame.Color("white"))
    for row in range(NUMBER_ROW):
        for column in range(NUMBER_COLUMN):
            if statusMatrix[row, column] == 1:
                pygame.draw.rect(screen, pygame.Color("black"), (column*CELL_SIZE, row*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    drawGrid(screen)
    screen.blit(ANT[antDirection], antCoordinate)
    pygame.display.flip()
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Langton's Ant")
    screen.fill(pygame.Color("white"))
    pygame.display.update()
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        event()
        update()
        displayScreen(screen)

if __name__ == '__main__':
    main()