import pygame

class Text:
    def __init__(self, left: int, top: int, width: int, height: int, text: str, boxcolor: pygame.color =None, textcolor: pygame.color =(0,0,0), font: pygame.font.SysFont = pygame.font.SysFont("Consolas", 25)) -> None:
        self.rect = pygame.Rect(left, top, width, height)
        self.boxcolor = boxcolor
        self.textcolor = textcolor
        self.font = font

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.textcolor)
        text_rect = text_surface.get_rect(center = self.rect.center)
        screen.blit(text_surface, text_rect)