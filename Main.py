from Tools import *
import Map

running = True
logger.write("Game started", logger.ACTION)


blocks = pygame.sprite.Group()

map = Map()
# Матрица с картой
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            logger.write("Game quited", logger.ACTION)
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
logger.write("Game exit", logger.ACTION)
