import pygame

from spiller import Spiller
from apple import Apple
from text import Text
from map import Map

pygame.init()

WIDTH, HEIGHT = 650, 650
FPS = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Consolas", 25)

snake = Spiller()
apples = [Apple([], snake.body), Apple([], snake.body)]
startbutton = Text(200, 50, 200, 100, "START", font, (255, 0, 0), (255,255,255), gamestate = "play")

map = Map(screen, WIDTH, HEIGHT, 50).make_map()
for tile in map:
    tile.rect.width = 50
    tile.surface.fill(tile.color)
    tile.give_coordinates()

game = "lost"
state = True
while state:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startbutton.handle_event(event.pos):
                game = startbutton.gamestate
    if game == "lost":
        snake = Spiller()
        apples = [Apple(apples, snake.body), Apple(apples, snake.body)]
        screen.fill((255,255,255))
        startbutton.draw(screen)
    else:
        keys = pygame.key.get_pressed()
        snake.input(keys)

        snake.update(apples)
        if snake.check_collision():
            game = "lost"

        while len(apples) < 2:
            apples.append(Apple(apples, snake.body))

        for tile in map:
            tile.draw(screen)
        snake.draw_body(screen)
        for apple in apples:
            apple.give_coordinates()
            apple.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()