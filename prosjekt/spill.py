import pygame
import sys
import random

from player import Player
from block import Block
from pokeball import Pokeball
from pokemon import Pokemon
import constants as c

# 1. Oppsett
pygame.init()

screen = pygame.display.set_mode((c.WIDTH,c.HEIGHT + c.EXTRA_HEIGHT))
clock = pygame.time.Clock()

# LAGER MAP
# LASTER BILDENE TIL MAPPET
stonesheet = pygame.image.load("images/stones.png").convert_alpha()
stone_height, stone_width = stonesheet.get_height(), stonesheet.get_width()
stone_width = 14
stone_height = 8
stones: list = []
for i in range(6):
    for o in range(3):
        temp_img = pygame.transform.scale_by(stonesheet.subsurface(o * stone_width + o * 2, i * stone_height + i, stone_width, stone_height), 3)
        stones.append(temp_img)
stone_width = stone_width*3
stone_height = stone_height*3

for _ in range(3):
    stones.remove(stones[6])
for _ in range(3):
    stones.remove(stones[6])

# KART KODE
with open("map.txt", "r") as f:
    data = f.read()
    data = data.split("\n")

# LAGER BLCOKGRUPPENE (MAPPET)
block_group = pygame.sprite.AbstractGroup()
standable_blocks = []



def make_block_group(map: list):
    for i in range(len(map)):
        for o in range(len(map[i])):
            if map[i][o] != "-":
                integer = int(map[i][o])
                block_group.add(Block(stones[integer - 1], o * stone_width - 5, (i-1) * stone_height + c.EXTRA_HEIGHT, False))
                if integer == 2:
                    block_group.add(Block(stones[integer + 2], o * stone_width, (i) * stone_height + c.EXTRA_HEIGHT, True))
                    standable_blocks.append(Block(stones[integer + 2], o * stone_width, (i) * stone_height + c.EXTRA_HEIGHT, True))
                else:
                    block_group.add(Block(stones[integer + 2], o * stone_width, (i) * stone_height + c.EXTRA_HEIGHT, False))
                block_group.add(Block(stones[integer + 5], o * stone_width, (i+1) * stone_height + c.EXTRA_HEIGHT, False))
                block_group.add(Block(stones[integer + 8], o * stone_width, (i+2) * stone_height + c.EXTRA_HEIGHT, False))

make_block_group(data)


# LAGER SPRITESHEETS FOR PLAYER (ASH)
ash_spritesheets = []
for i in range(1, 4):
    sheet = pygame.transform.scale_by(pygame.image.load(f"images/ash{i}.png").convert_alpha(), 0.3)
    ash_spritesheets.append(sheet)

player = Player(ash_spritesheets)

used_int = []
r_int = random.randint(0, len(standable_blocks) - 1)
pokeballs = []
pokeballs.append(Pokeball((standable_blocks[r_int].rect[0] + 0.5 * standable_blocks[r_int].rect[2], standable_blocks[r_int].rect[1] - 10)))
pokeballs.append(Pokeball((standable_blocks[r_int * -1].rect[0] + 0.5 * standable_blocks[r_int * -1].rect[2], standable_blocks[r_int * -1].rect[1] - 10)))

pokemen = []
pokemon_names = ["pikachu", "charizard"]
pokemen.append(Pokemon(pokemon_names[0], standable_blocks))

state = True
cooldown = 0

while state:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player.pokeballs > 0:
                mus_x, mus_y = pygame.mouse.get_pos()
                pokeballs.append(player.throw_pokeball(mus_x, mus_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and keys[pygame.K_d]:
        player.vel_x = 0
    elif keys[pygame.K_d]:
        player.vel_x = 4
    elif keys[pygame.K_a]:
        player.vel_x = -4
    else:
        player.vel_x = 0
    
    if keys[pygame.K_w]:
        if player.is_standing(block_group) and player.vel_y > -1:
            player.vel_y = -13

    
    cooldown -= 1
    if cooldown == 0:
        r_int = random.randint(0, len(standable_blocks) - 1)
        pokeballs.append(Pokeball((standable_blocks[r_int].rect[0] + 0.5 * standable_blocks[r_int].rect[2], standable_blocks[r_int].rect[1] - 10)))

    for pokeball in pokeballs:
        if player.rect.colliderect(pokeball.rect) and pokeball.throwed == False:
            pokeballs.remove(pokeball)
            player.pokeballs += 1
            cooldown = c.FPS
    
    # UPDATE
    if keys[pygame.K_s]:
        player.update(block_group, False)
    else:
        player.update(block_group)


    # DRAW
    screen.fill(c.GREY)
    # block_group.draw(screen)

    block_group.draw(screen)
    for pokemon in pokemen:
        pokemon.draw(screen)
    for pokeball in pokeballs:
        if pokeball.throwed:
            pokeball.update()
            for pokemon in pokemen:
                if pokeball.rect.colliderect(pokemon.rect):
                    pokeballs.remove(pokeball)
            
            if pokeball.rect.right < 0 or pokeball.rect.left > c.WIDTH or pokeball.rect.top > c.HEIGHT or pokeball.rect.bottom < 0:
                pokeballs.remove(pokeball)
        pokeball.draw(screen)
    player.draw(screen)

    screen.blit(pygame.font.SysFont("Consolas", 36).render(f"{player.pokeballs}", True, (255, 255, 255)), pygame.rect.Rect(0, c.HEIGHT + c.EXTRA_HEIGHT - 100, 100, 100))

    pygame.display.flip()
    clock.tick(c.FPS)

# QUIT PYGAME AND EXIT
pygame.quit()
sys.exit()