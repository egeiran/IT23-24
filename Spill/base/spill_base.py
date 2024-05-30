import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
FPS = 60

pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

state = True
while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    
    keys = pygame.key.get_pressed()

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()