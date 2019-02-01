from Tools import *
from Blocks import load_blocks
from Entity import Player

load_blocks()

running = True
logger.write("Game started", logger.ACTION)

clock = pygame.time.Clock()

entities = pygame.sprite.Group()
pl = Player(100, 100, entities)

while running:
    for event in pygame.event.get():
        pl.get_event(event)
        if event.type == pygame.QUIT:
            running = False
            logger.write("Game quited", logger.ACTION)
    screen.fill((0, 0, 0))
    entities.draw(screen)
    entities.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
logger.write("Game exited", logger.ACTION)
