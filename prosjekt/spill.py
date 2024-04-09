import pygame
import sys
import random

from player import Player
from block import Block
from pokeball import Pokeball
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
stones = []
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
                block_group.add(Block(stones[integer - 1], (o * stone_width - 5, (i-1) * stone_height + c.EXTRA_HEIGHT, stone_width, stone_height), False))
                if integer == 2:
                    block_group.add(Block(stones[integer + 2], (o * stone_width, (i) * stone_height + c.EXTRA_HEIGHT, stone_width, stone_height), True))
                    standable_blocks.append(Block(stones[integer + 2], (o * stone_width, (i) * stone_height + c.EXTRA_HEIGHT, stone_width, stone_height), True))
                else:
                    block_group.add(Block(stones[integer + 2], (o * stone_width, (i) * stone_height + c.EXTRA_HEIGHT, stone_width, stone_height), False))
                block_group.add(Block(stones[integer + 5], (o * stone_width, (i+1) * stone_height + c.EXTRA_HEIGHT, stone_width, stone_height), False))
                block_group.add(Block(stones[integer + 8], (o * stone_width, (i+2) * stone_height + c.EXTRA_HEIGHT, stone_width, stone_height), False))

make_block_group(data)


# LAGER SPRITESHEETS FOR PLAYER (ASH)
ash_spritesheets = []
for i in range(1, 4):
    sheet = pygame.transform.scale_by(pygame.image.load(f"images/ash{i}.png").convert_alpha(), 0.3)
    ash_spritesheets.append(sheet)

player = Player(ash_spritesheets)
pokeballs = pygame.sprite.AbstractGroup()
state = True

while state:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False

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
            for block in block_group:
                if player.is_standing(block_group):
                    player.vel_y = -13
    
    if len(pokeballs) < 3:
        used_int = []
        for i in range(3 - len(pokeballs)):
            while True:
                r_int = random.randint(0, len(standable_blocks) - 1)
                if r_int not in used_int:
                    used_int.append(r_int)
                    break
            pokeballs.add(Pokeball((standable_blocks[r_int].rect[0] + 0.5 * standable_blocks[r_int].rect[2], standable_blocks[r_int].rect[1] - 20)))

    print(pokeballs)
    for pokeball in pokeballs:
        if player.rect.colliderect(pokeball.rect):
            print("------------")
            print(pokeball)
            print("------------")
            player.pokeballs += 1
    

    # UPDATE
    player.update(block_group)

    # DRAW
    screen.fill(c.GREY)
    # block_group.draw(screen)
    for block in block_group:
        block.draw(screen)
    for pokeball in pokeballs:
        pokeball.draw(screen)
    player.draw(screen)
    

    pygame.display.flip()
    clock.tick(c.FPS)

# QUIT PYGAME AND EXIT
pygame.quit()
sys.exit()