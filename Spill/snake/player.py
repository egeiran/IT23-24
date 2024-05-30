import pygame
from bodypart import Bodypart

class Player():
    def __init__(self) -> None:
        self.vel_x = 1
        self.vel_y = 0
        head = Bodypart(6, 6, color=(0,0,255))
        self.body = [head]
        self.last_x = 0
        self.last_y = 0

    def move(self):
        self.last_pos_x = self.body[-1].x
        self.last_pos_y = self.body[-1].y

        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        self.body[0].x += self.vel_x
        self.body[0].y += self.vel_y

        self.last_dir_x = self.vel_x
        self.last_dir_y = self.vel_y

    def input(self, keys):
        if keys[pygame.K_UP] and self.last_dir_y != 1:
            self.vel_x = 0
            self.vel_y = -1
        if keys[pygame.K_LEFT] and self.last_dir_x != 1:
            self.vel_x = -1
            self.vel_y = 0
        if keys[pygame.K_DOWN] and self.last_dir_y != -1:
            self.vel_x = 0
            self.vel_y = 1
        if keys[pygame.K_RIGHT] and self.last_dir_x != -1:
            self.vel_x = 1
            self.vel_y = 0

    def check_apple(self, apples):
        for apple in apples:
            if apple.x == self.body[0].x and apple.y == self.body[0].y:
                apples.remove(apple)
                self.add_bodypart()
    
    def check_collision(self):
        for bodypart in self.body[1:]:
            if self.body[0].x == bodypart.x and self.body[0].y == bodypart.y:
                return True

    def add_bodypart(self):
        new_bodypart = Bodypart(self.last_pos_x, self.last_pos_y)
        self.body.append(new_bodypart)

    def update(self, apples):
        self.move()
        self.check_apple(apples)
        for bodypart in self.body:
            bodypart.give_coordinates()
    
    def draw_body(self, screen):
        for bodypart in self.body:
            bodypart.draw(screen)