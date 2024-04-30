import pygame
import math

import constants as c
from pokeball import Pokeball

def fart(x, y, desx, desy, velo):
    vinkel = math.atan2(desy-y,desx-x)
    velx = math.cos(vinkel)*velo
    vely = math.sin(vinkel)*velo
    return velx, vely

class Player():
    def __init__(self, spritesheets: pygame.sprite.Sprite) -> None:
        """
            Initierer et Player objekt
        """
        pygame.sprite.Sprite.__init__(self)
        # Bilder
        self.spritesheets = spritesheets
        self.image = self.spritesheets[-1]
        self.frame_index = 0
        self.rect: pygame.rect.Rect = self.image.get_rect()

        # Fart
        self.vel_x = 0
        self.vel_y = 0
        self.acc_y = c.acc_y
        
        self.y = 300
        self.x = 300
        
        # Pokeball 
        pokeball_image = pygame.transform.scale_by(pygame.image.load("images/pokeball.png").convert_alpha(), 0.015)


        # Annet
        self.update_time = pygame.time.get_ticks()
        self.animation_list_left, self.animation_list_right = self.load_animations()
        self.liv = 3
        self.pokeballs = 0

    def load_animations(self):
        """
            Returnerer lister bestående av bildene til animasjonene
        """
        animation_list_left = []
        size_x = self.spritesheets[0].get_width()/3
        size_y = self.spritesheets[0].get_height()
        for x in range(3):
            temp_img = self.spritesheets[0].subsurface(x * size_x, 0, size_x, size_y)
            animation_list_left.append(temp_img)
        animation_list_right = []
        size_x = self.spritesheets[1].get_width()/3
        size_y = self.spritesheets[1].get_height()
        for x in range(3):
            temp_img = self.spritesheets[1].subsurface(x * size_x, 0, size_x, size_y)
            animation_list_right.append(temp_img)
        return animation_list_left, animation_list_right

    def play_animations(self):
        """
            Utfører animasjonen dersom spilleren beveger seg i x-retning
        """
        if self.vel_x > 0:
            # LAG ANIMASJON MOT HØYRE
            if pygame.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # CHECK IF ANIMATION IS FINISHED
            if self.frame_index >= len(self.animation_list_right):
                self.frame_index = 0
            self.image = self.animation_list_right[self.frame_index]
        elif self.vel_x < 0:
            # LAG ANIMASJON MOT VENSTRE
            if pygame.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
            # CHECK IF ANIMATION IS FINISHED
            if self.frame_index >= len(self.animation_list_left):
                self.frame_index = 0
            self.image = self.animation_list_left[self.frame_index]
        else:
            self.image = self.spritesheets[2]

    def is_standing(self, blocks: list):
        """
            Sjekker om self står på en block
        """
        for block in blocks:
            if block.standable:
                if self.rect.colliderect(block.rect) and self.rect.bottom < block.standheight + 15:
                    self.y = block.standheight
                    return True
        return False

    def throw_pokeball(self, mus_x, mus_y):
        self.pokeballs -= 1
        vel_x, vel_y = fart(self.rect.centerx, self.rect.centery, mus_x, mus_y, 15)
        return Pokeball((self.rect.centerx, self.rect.centery), True, vel_x, vel_y)

    def update(self, blocks):
        """
            Oppdaterer posisjon, bilde og tilstand til karakteren
        """
        self.x += self.vel_x
        if self.is_standing(blocks) and self.vel_y >= 0:
            self.vel_y = 0
        else:
            self.vel_y += self.acc_y
            if self.vel_y >= 20:
                self.vel_y = 20
            self.y += self.vel_y
        self.play_animations()

    def draw(self, screen):
        """
            Blitter bildet til karakteren på skjermen
        """
        self.rect.bottom = self.y
        self.rect.centerx = self.x
        screen.blit(self.image, self.rect)