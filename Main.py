from Tools import *


running = True
logger.log("Game started", logger.ACTION)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            logger.write("Game quited", logger.ACTION)
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
logger.write("Game exit", logger.ACTION)
