from Tools import *
from Map import Map
from Blocks import load_blocks
from Entity import Player

load_blocks()

running = True
logger.write("Game started", logger.ACTION)


blocks = pygame.sprite.Group()

load_blocks()


board = [[0] * 19, [1] * 19] * 18 + [[0] * 19]
print(board)
map = Map(board, blocks)
map.generate_map()
# Матрица с картой
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
    blocks.draw(screen)
    entities.draw(screen)
    entities.update()
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
logger.write("Game exited", logger.ACTION)
