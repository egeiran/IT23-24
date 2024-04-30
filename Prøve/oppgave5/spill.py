import pygame
import sys
import random

from racket import Racket
from ball import Ball
from objekt import Objekt

# 1. Oppsett
pygame.init()

WIDTH, HEIGHT = 1200, 800
FPS = 60

font = pygame.font.Font(None, 100)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player1 = Racket(True)
player2 = Racket(False)
rackets = [player1, player2]
balliste = [Ball()]

hindringer = []
for i in range(3):
    if random.randint(0,1) == 1:
        hindringer.append(Objekt(((WIDTH - 12)/2, random.randint(2, HEIGHT/2 - 10 - 80), 12, 80)))
    else:
        hindringer.append(Objekt(((WIDTH - 12)/2, random.randint(HEIGHT/2 + 10, HEIGHT - 2), 12, 80)))

# GAMELOOP
state = True
while state:
    # 2. Håndter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    keys = pygame.key.get_pressed()
    # VENSTRE
    if keys[pygame.K_w] and keys[pygame.K_s]:
        pass
    elif keys[pygame.K_w]:
        player1.flytt(-1)
        if player1.rect.top < 2:
            player1.rect.top = 2
    elif keys[pygame.K_s]:
        player1.flytt(1)
        if player1.rect.bottom > 798:
            player1.rect.bottom = 798

    # HØYRE
    if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
        pass
    elif keys[pygame.K_UP]:
        player2.flytt(-1)
        if player2.rect.top < 2:
            player2.rect.top = 2
    elif keys[pygame.K_DOWN]:
        player2.flytt(1)
        if player2.rect.bottom > 798:
            player2.rect.bottom = 798
        
    for ball in balliste:
        ball.update()

    # SJEKK KOLLISJON MED RACKET
    for racket in rackets:
        for ball in balliste:
            if ball.rect.colliderect(racket.rect):
                ball.vel_x = ball.vel_x * -1
                if racket.left:
                    ball.rect.left = racket.rect.right + 1
                else:
                    ball.rect.right = racket.rect.left - 1
                if len(balliste) < 5:
                    balliste.append(Ball(ball.rect.left, ball.rect.top))
    
    # SJEKK KOLLISJON MED TAK/GULV OG HINDRINGER
    for ball in balliste:
        if ball.rect.top <= 0:
            ball.vel_y = ball.vel_y * -1
        if ball.rect.bottom >= HEIGHT:
            ball.vel_y = ball.vel_y * -1
        for hindring in hindringer:
            if ball.rect.colliderect(hindring.rect):
                ball.vel_x = ball.vel_x * -1
                if ball.rect.centery < hindring.rect.top:
                    ball.vel_y = ball.vel_y * -1
                elif ball.rect.centery > hindring.rect.bottom:
                    ball.vel_y = ball.vel_y * -1

    # SJEKK FOR MÅL
    for ball in balliste:
        if ball.rect.right <= 0:
            balliste.remove(ball)
            player2.score += 1
        if ball.rect.left >= WIDTH:
            balliste.remove(ball)
            player1.score += 1
    if len(balliste) == 0:
        balliste.append(Ball())
    

    # Tegn
    screen.fill((0,0,0))
    for i in range(40):
        pygame.draw.rect(screen, (100,100,100), ((1200-10)/2, 3 + i * 20, 10, 10))
    for racket in rackets:
        racket.draw(screen)
    for ball in balliste:
        ball.draw(screen)
    for hindring in hindringer:
        hindring.draw(screen)
    screen.blit(font.render(str(player1.score), True, (100, 100, 100)), (510, 20, 50, 50))
    screen.blit(font.render(str(player2.score), True, (100, 100, 100)), (650, 20, 50, 50))

    pygame.display.flip()
    clock.tick(FPS)

# QUIT PYGAME AND EXIT
pygame.quit()
sys.exit()