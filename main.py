import pygame, sys
from simulation import Simulation
pygame.init()

screenWidth = 750
screenHeight = 750
cellSize = 25

darkGrey = (29,29,29)

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(screenWidth, screenHeight, cellSize)

fps = 12

# sim loop

while True:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            row = pos[1] // cellSize
            col = pos[0] // cellSize
            
            simulation.toggleCell(row, col)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                simulation.start()
            if event.key == pygame.K_SPACE:
                simulation.stop()
            if event.key == pygame.K_w:
                fps += 2
            if event.key == pygame.K_s:
                if fps > 5:
                    fps -= 2
            if event.key == pygame.K_r:
                simulation.createRandomState()
            if event.key == pygame.K_c:
                simulation.clear()
    #update
    simulation.update()
    #draw
    screen.fill(darkGrey)
    simulation.draw(screen)
    pygame.display.update()
    
    clock.tick(fps)
